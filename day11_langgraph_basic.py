import os
os.environ["HF_HUB_OFFLINE"] = "1"

from typing import TypedDict
from langgraph.graph import StateGraph,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    question: str
    answer: str

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3",
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    temperature=0.7,
)

def ask_note(state: State):
    prompt = ChatPromptTemplate.from_template("你是一个知识助手。问题: {question}")
    chain = prompt | llm | StrOutputParser()
    answer = chain.invoke({"question": state["question"]})
    return {"answer": answer}

graph = StateGraph(State)
graph.add_node("ask",ask_note)
graph.set_entry_point("ask")
graph.add_edge("ask",END)
app=graph.compile()
result = app.invoke({"question": "LangGraph和Langchain Chain的区别"})
print(f"问题: {result['question']}")
print(f"回答: {result['answer']}")

