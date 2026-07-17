from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embedder = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
)

vector = embedder.embed_query("人工智能正在改变世界")

print(vector)
print(f"向量维度: {len(vector)}")
print(f"前5个元素: {vector[:5]}")
print(f"类型: {type(vector[0])}")

#要是没环境就在终端运行下面代码
# $env:HF_ENDPOINT="https://hf-mirror.com" （设置本地环境变量）
# python day9_embed_local.py
