from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embedder = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedder,
)

query = "人工智能正在改变世界"
results=vectorstore.similarity_search(
    query=query,
    k=2,
)

for i,doc in enumerate(results):
    print(f"——结果{i+1}——")
    print(doc.page_content)
    print("\n")