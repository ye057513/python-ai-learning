from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url=os.getenv("SILICONFLOW_API_BASE"),
    model="deepseek-ai/DeepSeek-V4-Pro",
)

prompt=ChatPromptTemplate.from_messages([
    ("system","你是一个专业的翻译，只输出翻译结果，不需要解释"),
    ("user","把下面的话翻译成{language}:\n{text}"),
])
chain=prompt|llm

result=chain.invoke({"language":"日语","text":"人工智能正在改变世界"})
print(result)
