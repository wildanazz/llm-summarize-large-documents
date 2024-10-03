---

# LLM Summarize Large Documents

This repository provides scripts to summarize large documents using Language Learning Models (LLMs). It includes two main Python files that implement different document summarization techniques.

## Files

1. **MapReduceChain.py**:
   - Utilizes a MapReduce approach to break down large documents into manageable chunks, summarize them individually, and combine the results.
   
2. **StuffDocumentChain.py**:
   - Implements the "stuff" chain method where smaller document sections are summarized collectively.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wildanazz/llm-summarize-large-documents.git
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- To summarize a document using MapReduce:
  ```bash
  python MapReduceChain.py --input your_document.txt
  ```
- To use StuffDocumentChain:
  ```bash
  python StuffDocumentChain.py --input your_document.txt
  ```

## License

This project is open-source and free to use.

---
