from dotenv import load_dotenv
from langchain_together import ChatTogether
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import StuffDocumentsChain, LLMChain, ReduceDocumentsChain, MapReduceDocumentsChain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import TokenTextSplitter

load_dotenv()

llm = ChatTogether()

# Map Chain
map_prompt = ChatPromptTemplate.from_template(
    "Write a concise summary of the following content and provide the output in bullet points: {context}")

map_chain = LLMChain(prompt=map_prompt, llm=llm)

# Reduce Chain
reduce_prompt = ChatPromptTemplate.from_template(
    "Summarize the following set of summaries in paragraphs with all the key details: {context}")

reduce_chain = LLMChain(prompt=reduce_prompt, llm=llm)

combine_documents_chain = StuffDocumentsChain(
    llm_chain=reduce_chain, document_variable_name="context")
reduce_chain = ReduceDocumentsChain(
    combine_documents_chain=combine_documents_chain,
)

# Map Reduce Chain
map_reduce_chain = MapReduceDocumentsChain(
    llm_chain=map_chain,
    document_variable_name="context",
    reduce_documents_chain=reduce_chain
)

# Load external website's content
loader = WebBaseLoader(
    'https://python.langchain.com/docs/get_started/introduction')
docs = loader.load()

# Split the content into smaller chunks
splitter = TokenTextSplitter(chunk_size=2000)
split_docs = splitter.split_documents(docs)

# Use map reduce chain to summarize
result = map_reduce_chain.run(split_docs)
print(result)
