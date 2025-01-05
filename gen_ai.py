import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import PyPDF2
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


# Step 1: Parse the PDF
def parse_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Step 2: Initialize the embedding model (GoogleGenerativeAIEmbeddings)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Step 3: Prepare the document text (from the PDF)
document_text = parse_pdf("data/Analytics_vidya_courses.pdf")  # Path to your PDF file

# Step 4: Generate embeddings for the document text using the GoogleGenerativeAIEmbeddings
vector = embeddings.embed_query(document_text)


document = Document(page_content=document_text)

# Step 5: Manually store embeddings in a Chroma vector store
# Assuming the vector is a list of embeddings, and you want to store them.
vector_store = Chroma.from_documents(
    [document],  # Document list
    embedding=embeddings,  # Embedding model
    persist_directory="./persisted_vector_store"  # Specify directory to persist vectors
)


chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Step 6: Set up Langchain QA pipeline with Google's generative AI model
qa_chain = load_qa_chain(chat_model, chain_type="stuff")


