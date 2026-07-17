from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_API_BASE_URL"),
    model="deepseek-ai/DeepSeek-V4-Pro",
    timeout=60,
)

vector = embeddings.embed_query("人工智能正在改变世界")

print(vector)
print(f"向量维度: {len(vector)}")
print(f"前5个元素: {vector[:5]}")
print(f"类型: {type(vector[0])}")