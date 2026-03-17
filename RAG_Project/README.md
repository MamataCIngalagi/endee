# AI RAG Chatbot using Endee

<p align="center">
  <b>Semantic Search-based University Assistant using Retrieval-Augmented Generation (RAG)</b>
</p>

 <p align="center">
<strong>
<a href="#overview">Overview</a> •
<a href="#problem-statement">Problem Statement</a> •
<a href="#tech-stack">Tech Stack</a> •
<a href="#how-it-works">How It Works</a> •
<a href="#project-structure">Structure</a> •
<a href="#how-to-run">Run</a>
</strong>
</p>

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers university-related queries using semantic search and vector embeddings.

## Problem Statement
Students often struggle to find accurate information about university rules, exams, placements, and facilities.  
This chatbot solves the problem by retrieving the most relevant answer from a dataset using vector similarity search.

## Tech Stack
- Python  
- Sentence Transformers  
- NumPy  
- Endee (Vector Database Concept)  

## How It Works
1. FAQ dataset is split into question-answer pairs  
2. Each pair is converted into embeddings using Sentence Transformers  
3. Embeddings are stored in a vector structure (Endee-inspired)  
4. User query is converted into embedding  
5. Similarity search retrieves the most relevant answer  

## Project Structure
```
RAG_Project/
|-- app.py
|-- faq.txt
|-- requirements.txt
|-- README.md
```

## How to Run
```
pip install -r requirements.txt
python app.py
```

## Example Queries
- What is the minimum attendance required?  
- How can I apply for placements?  
- What are the library working hours?  

## Features
- Semantic search using embeddings  
- Fast retrieval of relevant answers  
- Lightweight RAG pipeline  
- Handles multiple university-related queries  

## Future Improvements
- Integration with full Endee vector database  
- Web interface (Gradio / Streamlit)  
- Support for large-scale datasets  

## Conclusion
This project demonstrates how Retrieval-Augmented Generation (RAG) can be used to build intelligent question-answering systems using vector similarity search.

## Note
This project uses an Endee-inspired vector storage approach and can be extended to integrate directly with the Endee vector database.
