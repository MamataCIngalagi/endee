from sentence_transformers import SentenceTransformer
import numpy as np

# Load FAQ file
with open("faq.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chunks (Q&A pairs)
chunks = text.strip().split("\n\n")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert chunks into embeddings
embeddings = model.encode(chunks)

# Function to find best answer
def get_answer(query):
    query_embedding = model.encode([query])
    
    # Compute similarity (dot product)
    similarities = np.dot(embeddings, query_embedding.T).flatten()
    
    best_index = np.argmax(similarities)
    best_chunk = chunks[best_index]

    if "A:" in best_chunk:
        return best_chunk.split("A:")[1].strip()
    else:
        return best_chunk

# Chat loop
print("University RAG Chatbot (type 'exit' to quit)\n")

while True:
    user_query = input("Ask a question: ")
    
    if user_query.lower() == "exit":
        break
    
    answer = get_answer(user_query)
    print("Answer:", answer, "\n")
