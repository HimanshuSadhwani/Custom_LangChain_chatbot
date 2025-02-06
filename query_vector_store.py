import faiss
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
import numpy as np

def query_vector_store(query):
    # Load the FAISS index from the file
    index = faiss.read_index("vector_store.index")
    
    # Use Hugging Face embeddings to embed the query text
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)
    embeddings = HuggingFaceEmbeddings(model)
    
    # Convert the query text into an embedding
    query_embedding = embeddings.embed_query(query)
    
    # Convert query embedding to numpy array
    query_embedding = np.array(query_embedding).reshape(1, -1)
    
    # Perform a similarity search
    D, I = index.search(query_embedding, k=3)  # 'k' is the number of nearest neighbors to retrieve

    # Print the closest matches (retrieve the text corresponding to the indices)
    print(f"Closest Matches (Indices): {I}")
    print(f"Distances (D): {D}")

if __name__ == "__main__":
    query_text = "Python programming basics"
    query_vector_store(query_text)
