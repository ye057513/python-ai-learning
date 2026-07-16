from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import asyncio
import time

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

async def tell_story(topic:str):
    chain=prompt|llm
    print(f"\n=== {topic} ===\n")
    async for chunk in chain.astream({'topic':topic}):
        print(chunk.content,end="",flush=True)
        print("\n")
        await asyncio.sleep(0.1)


async def main():
    print("AI正在写作...\n")
    result=await asyncio.gather(
        tell_story("一只勇敢的猫"),
        tell_story("一只勇敢的狗"),
        tell_story("一只勇敢的鱼"),
    )
    print("\n\n故事结束。")
    return result

asyncio.run(main())