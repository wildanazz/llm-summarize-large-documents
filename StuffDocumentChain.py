from dotenv import load_dotenv
from langchain_together import ChatTogether
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

llm = ChatTogether()

prompt = ChatPromptTemplate.from_template(
    "Write a concise summary of the following content and provide the output in bullet points: {context}")

chain = create_stuff_documents_chain(llm, prompt)

# Load external website's content
loader = WebBaseLoader(
    'https://python.langchain.com/docs/get_started/introduction')
docs = loader.load()

result = chain.invoke({"context": docs})
print(result)
