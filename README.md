Medical Chatbot

A Retrieval-Augmented Generation (RAG) based medical chatbot that answers questions using information retrieved from a medical knowledge base.

Features

- Medical question answering
- PDF-based knowledge base
- Hugging Face embeddings
- Pinecone vector database
- LangChain-based RAG pipeline
- Groq-powered language model
- Flask web application
- Simple chat interface

Project Structure

Medical-Chatbot/
├── app.py
├── store_index.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── README.md
├── .env
├── Data/
├── research/
│   └── trials.ipynb
├── src/
│   ├── _init_.py
│   ├── helper.py
│   └── prompt.py
├── templates/
│   └── chat.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js

Setup

1. Clone the repository

git clone https://github.com/DeepTensor-3070/Medical-Chatbot.git
cd Medical-Chatbot

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create a ".env" file in the project root:

PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key

Do not commit ".env" to GitHub.

5. Add the medical PDF

Place the medical PDF inside:

Data/

6. Upload the knowledge base to Pinecone

Run:

python store_index.py

7. Start the application

Run:

python app.py

Then open:

http://127.0.0.1:8080

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
Flask Application
    ↓
Chat Interface

Disclaimer

This project is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.