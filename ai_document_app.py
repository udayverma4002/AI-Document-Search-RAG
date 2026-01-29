import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="AI Document Search", layout="wide")
st.title("📄 AI Based Document Search & RAG")

st.write("Upload a document and ask questions from it.")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

documents = []

if uploaded_file:
    file_path = uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    documents = loader.load()
    st.success("Document loaded successfully!")

if documents:
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    question = st.text_input("Ask a question from the document")

    if question:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=api_key,
            temperature=0.2
        )

        context = "\n".join([c.page_content for c in chunks[:3]])

        prompt = f"""
        Answer the question using only the context below.

        Context:
        {context}

        Question:
        {question}
        """

        response = llm.invoke(prompt)
        st.subheader("Answer")
        st.write(response.content)
