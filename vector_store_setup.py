from transformers import AutoModel, AutoTokenizer
import faiss
import numpy as np
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_store(texts):
    # Load the Hugging Face model and tokenizer
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Use HuggingFaceEmbeddings with Hugging Face model and tokenizer
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    # Convert texts to embeddings
    text_embeddings = embeddings.embed_documents(texts)

    # Convert embeddings to numpy array
    text_embeddings = np.array(text_embeddings)

    # Initialize FAISS index
    index = faiss.IndexFlatL2(text_embeddings.shape[1])

    # Add embeddings to FAISS index
    index.add(text_embeddings)

    # Save the FAISS index to a file
    faiss.write_index(index, "vector_store.index")
    print("Vector store created and saved successfully!")

if __name__ == "__main__":
    # Example texts
    course_texts = [
        "Introduction to Python Programming",
        "Data Structures and Algorithms Course",
        "Web Development with Flask and Django",
        "Machine Learning for Beginners"
    ]
    create_vector_store(course_texts)
