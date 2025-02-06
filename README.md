# Custom LC Chatbot

This project is a Flask-based chatbot powered by LangChain, FAISS, and OpenAI. It extracts course data, creates embeddings, stores them in a vector store, and provides a RESTful API for conversational interactions.

## Features
- Extracts data from websites.
- Generates embeddings with HuggingFace Sentence Transformers.
- Stores embeddings in FAISS vector store.
- Implements a conversational chatbot API using Flask.

## Prerequisites
- Python 3.9+
- OpenAI API Key (Sign up at [OpenAI](https://platform.openai.com/))
- Clone this repository:
  ```bash
  git clone https://github.com/yourusername/custom-lc-chatbot.git
  cd custom-lc-chatbot
Installation
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your OpenAI API key to an .env file:

env
Copy
Edit
OPENAI_API_KEY=your-openai-api-key
Usage
Data Extraction Run data_extraction.py to extract data from a target website:

bash
Copy
Edit
python data_extraction.py
Create Vector Store Use vector_store_setup.py to generate the vector store:

bash
Copy
Edit
python vector_store_setup.py
Query the Vector Store Test the vector store by running:

bash
Copy
Edit
python query_vector_store.py
Start the Chatbot API Launch the Flask API using:

bash
Copy
Edit
python app.py
The API will be available at http://127.0.0.1:5000.

Test the Chatbot Use Postman or cURL to interact with the chatbot:

Endpoint: POST /chatbot
Example Body:
json
Copy
Edit
{
  "user_input": "Hello, what can you do?"
}
Files
app.py: Flask API for chatbot interaction.
vector_store_setup.py: Script to create and store embeddings in FAISS.
query_vector_store.py: Script to query the FAISS vector store.
data_extraction.py: Script for extracting data from websites.
