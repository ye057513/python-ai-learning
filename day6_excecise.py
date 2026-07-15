from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
#AI生成菜谱
llm=ChatOpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_API_BASE"),
    model="deepseek-ai/DeepSeek-V4-Pro",
)

prompt=ChatPromptTemplate.from_messages([
    ("system","你是一名专业的厨师,我需要你帮我生成下面输入菜品的菜谱"),
    ("user","{dish_name}:{dish_description}"),
])
chain=prompt|llm
dish_name=input("请输入菜品名称:")
dish_description=input("请输入口味偏好:")

result=chain.invoke({"dish_name":dish_name,"dish_description":dish_description})
print(result)