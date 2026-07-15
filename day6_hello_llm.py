from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatOpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_API_BASE"),
    model="deepseek-ai/DeepSeek-V4-Pro",
)

response=llm.invoke("你好，我是张三")
print(response)