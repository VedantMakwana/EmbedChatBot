# Importing important liblary
import os
import pickle
from contextlib import contextmanager
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from transformers import AutoModel
from langchain_huggingface import HuggingFaceEndpoint
from langchain.document_loaders import WebBaseLoader
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain import hub


# Load environment variables
load_dotenv()

# Function to safely manage file operations
@contextmanager
def open_file(filename, mode='rb'):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()


# URL to fetch data
url_address = "https://brainlox.com/courses/category/technical"


try:
    # Fetch web content
    web_loader = WebBaseLoader(url_address)
    page_content = web_loader.load()
except Exception as e:
    print(f"Error loading web content: {e}")
    exit(1)

# Split data into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,  # Adjusted chunk size
    chunk_overlap=100  # Adjusted overlap
)
texts = text_splitter.split_documents(page_content)

# Function to store FAISS vector store
def store_embedding(docs, embeddings, store_name, path):
    vector_store = FAISS.from_documents(docs, embeddings)
    with open_file(f"{path}/faiss_{store_name}.pkl", "wb") as f:
        pickle.dump(vector_store, f)

# Function to load FAISS vector store
def load_embeddings(store_name, path):
    with open_file(f"{path}/faiss_{store_name}.pkl", "rb") as f:
        vector_store = pickle.load(f)
    return vector_store

model_name = "hkunlp/instructor-xl"
model_kwargs = {'device': 'cpu'}
hf = HuggingFaceInstructEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs
)

# # Create and save the vector store
# store_embedding(docs=texts,
#                 embeddings=hf,
#                 store_name="instructor_embedding",
#                 path="Embedding_store")


# # Alternatively, load the vector store
# db_instructEmbedd = load_embeddings(store_name="instructor_embedding",
#                                     path="Embedding_store")

# Create FAISS directly
db_instructEmbedd = FAISS.from_documents(texts, hf)


# Create retriever object
retriever = db_instructEmbedd.as_retriever(search_kwargs={"k": 3})

# Hugging Face Endpoint model setup
token = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = token
repo_id = "openai-community/gpt2"


try:
    llm_model = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.7, max_new_tokens=128, token=token)
except Exception as e:
    print(f"Error initializing Hugging Face endpoint: {e}")
    exit(1)

# Define Flask RESTful resource

class Conversation(Resource):
    def post(self):
        json_data = request.get_json()
        question = json_data.get('question')

        # Function to handle response
        def llm_responces(question, retriever=retriever, llm_model=llm_model):
            prompt = hub.pull("rlm/rag-prompt", api_url="https://api.hub.langchain.com")
            dbqa = RetrievalQA.from_chain_type(llm=llm_model,
                                               chain_type="stuff",
                                               retriever=retriever,
                                               return_source_documents=True,
                                               chain_type_kwargs={"prompt": prompt})
            response = dbqa({"query": question})
            return response["result"]

        # Get response
        response = llm_responces(question)
        return jsonify({"response": response})
