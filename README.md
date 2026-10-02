Medical Chatbot

A Retrieval-Augmented Generation (RAG) based medical chatbot that uses a medical knowledge base to retrieve relevant information and generate answers to user questions.

Features

- Medical question answering
- PDF-based medical knowledge base
- Hugging Face embeddings
- Pinecone vector database
- LangChain-based RAG pipeline
- Groq-powered language model
- Flask web application
- Simple and interactive chat interface

Project Structure

Medical-Chatbot/
│
├── app.py
├── store_index.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── .gitignore
│
├── Data/
│   └── medical PDF
│
├── research/
│   └── trials.ipynb
│
├── src/
│   ├── _init_.py
│   ├── helper.py
│   └── prompt.py
│
├── templates/
│   └── chat.html
│
└── static/
    └── style.css

Requirements

- Python 3.12.x
- Pinecone account and API key
- Groq API key
- Internet connection

Installation

Create a virtual environment:

python -m venv .venv

Activate the virtual environment on Windows:

.venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Environment Variables

Create a ".env" file in the project root and add:

PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key

Do not upload the ".env" file to GitHub because it contains API credentials.

Medical Knowledge Base

Place the required medical PDF inside the "Data" folder:

Data/
└── medical_book.pdf

The PDF is processed into smaller text chunks, converted into embeddings, and stored in the Pinecone vector database.

Indexing the Documents

After adding the medical PDF, run:

python store_index.py

This uploads the document embeddings to the Pinecone index.

Running the Chatbot

Start the Flask application:

python app.py

The application will run locally at:

http://127.0.0.1:8080

Open the address in a web browser to use the chatbot.

Architecture

Medical PDF
     ↓
Document Loading
     ↓
Text Splitting
     ↓
Hugging Face Embeddings
     ↓
Pinecone Vector Database
     ↓
Retriever
     ↓
Groq LLM
     ↓
Flask Backend
     ↓
Chat Interface

Working

1. The medical PDF is loaded from the "Data" folder.
2. The document is divided into smaller text chunks.
3. The chunks are converted into vector embeddings.
4. The embeddings are stored in Pinecone.
5. When a user asks a question, relevant information is retrieved from Pinecone.
6. The retrieved information is provided to the language model.
7. The generated response is displayed through the Flask chat interface.

Disclaimer

This project is intended for educational and informational purposes only.

The chatbot is not a substitute for professional medical advice, diagnosis, or treatment. Users should consult a qualified healthcare professional for medical concerns.