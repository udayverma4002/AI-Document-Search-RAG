# AI Based Document Search and Knowledge Retrieval

This project is an AI-based document reader that allows users to upload documents
and ask questions to get accurate answers using RAG and Large Language Models.

## Features
- Upload PDF, DOCX, PPTX, TXT, and Image files
- AI-based question answering
- Retrieval Augmented Generation (RAG)
- Multi-turn conversation support
- Document analytics and usage tracking
- Role-based authentication (demo)

## Technologies Used
- Python
- Streamlit
- LangChain
- Google Gemini (LLM)
- RAG Architecture
- PyPDF, OCR, Transformers

## How It Works
1. User uploads documents
2. Text is extracted and processed
3. Documents are chunked and indexed
4. Relevant content is retrieved
5. LLM generates document-based answers

## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`

2. Create `.env` file using `.env.example`

3. Run the app  
   `streamlit run ai_document_app.py`

## Security
- API keys are stored using environment variables
- `.env` file is excluded from GitHub
