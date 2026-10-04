from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from src.prompt import system_prompt
import os


app = Flask(__name__)

load_dotenv()


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is not set")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


embeddings = download_hugging_face_embeddings()


index_name = "medicalbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name, embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})


llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {
        "context": retriever | format_docs,
        "input": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)
# EMERGENCY DETECTION
# ============================================================

EMERGENCY_KEYWORDS = [
    "severe chest pain",
    "chest pain and difficulty breathing",
    "difficulty breathing",
    "cannot breathe",
    "can't breathe",
    "severe breathing problem",
    "unconscious",
    "not responding",
    "seizure",
    "stroke",
    "severe bleeding",
    "heavy bleeding",
    "fainted and not recovering",
    "saans nahi aa rahi",
    "saans lene mein dikkat",
    "seene mein bahut tez dard",
    "seene me bahut tez dard",
    "behosh",
    "fit aa raha",
    "bahut zyada khoon"
]


def is_emergency(message):
    message = message.lower()

    for keyword in EMERGENCY_KEYWORDS:
        if keyword in message:
            return True

    return False


# ============================================================
# EMERGENCY RESPONSE
# ============================================================

EMERGENCY_RESPONSE = """
🚨 <strong>Possible Medical Emergency</strong>

The symptoms you described may require urgent medical attention.

Please contact your local emergency service or go to the nearest emergency department immediately.

Do not rely on this chatbot for emergency diagnosis or treatment.
"""





@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():

    msg = request.form.get("msg", "").strip()

    if not msg:
        return "Please enter a question."

    print("Question:", msg)
    if is_emergency(msg):
        print("Emergency query detected")
        return EMERGENCY_RESPONSE

    response = rag_chain.invoke(msg)

    print("Response:", response)

    return response



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)