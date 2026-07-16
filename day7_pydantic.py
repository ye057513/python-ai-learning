from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field

load_dotenv()

class Person(BaseModel):
    name: str=Field(description="姓名")
    age:int=Field(description="年龄")
    skill:list[str]=Field(description="技能列表")
    city:str=Field(description="城市")

llm=ChatOpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_API_BASE"),
    model="deepseek-ai/DeepSeek-V4-Pro",
    temperature=0,
)

parser=StrOutputParser(pydantic_object=Person)

prompt=ChatPromptTemplate.from_messages([
    ("system","提取用户信息。\n{format_instructions}"),
    ("user","{text}"),
])

chain=prompt|llm|parser

result=chain.invoke({"text":"我叫李明，28岁，住在厦门，精通React和Node.js", 
                      "format_instructions":Person.model_json_schema()
                      })
print(result)
print(f"类型:{type(result).__name__}")