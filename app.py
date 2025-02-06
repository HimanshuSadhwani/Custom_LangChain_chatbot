from flask import Flask, request, jsonify
import faiss
import os
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.schema import Document
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# Load the FAISS index
index = faiss.read_index("vector_store.index")
if not os.path.exists("vector_store.index"):
    raise FileNotFoundError("FAISS index file not found.")


# Properly initialize the document store
docstore = InMemoryDocstore({})

# Set up an empty index-to-docstore mapping for FAISS compatibility
index_to_docstore_id = {i: str(i) for i in range(index.ntotal)}

# Load embedding function
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_function = HuggingFaceEmbeddings(model_name=model_name)

# Proper FAISS initialization
vector_store = FAISS(
    embedding_function=embedding_function,
    index=index,
    docstore=docstore,
    index_to_docstore_id=index_to_docstore_id
)

# Initialize the LLM
llm = OpenAI(openai_api_key=os.getenv("sk-abcdef1234567890abcdef1234567890abcdef12"))

# Define QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(),
    chain_type="stuff",
)

# Add base route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Custom LC Chatbot API! Available endpoint: POST /chatbot"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    if not data or "user_input" not in data:
        return jsonify({"error": "Please provide a user_input key with a message"}), 400

    user_input = data["user_input"]
    return jsonify({"response": f"Received: {user_input}"})



if __name__ == "__main__":
    app.run(debug=True)
