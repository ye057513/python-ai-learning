# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("test.txt",encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
)

chunks = splitter.split_documents(docs)

embedder = HuggingFaceEmbeddings(
    # model="deepseek-ai/DeepSeek-V4-Pro",
    # base_url=os.getenv("SILICONFLOW_API_BASE_URL"),
    # api_key=os.getenv("SILICONFLOW_API_KEY"),
    model_name="BAAI/bge-small-zh-v1.5",
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedder,
    persist_directory="./chroma_db",
)

print(f"入库完成，共入库{len(chunks)}个文档")
