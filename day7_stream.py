from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_API_BASE"),
    model="deepseek-ai/DeepSeek-V4-Pro",
    temperature=0.7,
    streaming=True,
)

prompt=ChatPromptTemplate.from_messages([
    ("system","你是一个故事作家,每个回答不少于200个字。"),
    ("user","写一个关于{topic}的故事"),
])
chain=prompt|llm

print("AI正在写作...\n")

for chunk in chain.stream(('topic','一只勇敢的猫')):
    print(chunk.content,end="",flush=True)

print("\n\n故事结束。")
