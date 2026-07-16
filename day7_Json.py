from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatOpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_API_BASE"),
    model="deepseek-ai/DeepSeek-V4-Pro",
    temperature=0,
)

prompt=ChatPromptTemplate.from_messages([
    ("system","""你是一个数据分析助手。根据输入的文字，提取关键信息并以JSON格式返回。"
    "JSON输出格式：{{"name":"姓名","age":年龄,"skill":["技能1","技能2"]}}只返回JSON格式，不要解释。"""),
    ("user","{text}"),
    ])

parser=StrOutputParser()

chain=prompt|llm|parser

result=chain.invoke({"text":"张三今年18岁，他喜欢篮球"})
print(result)
print(type(result))