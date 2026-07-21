import os
os.environ["HF_HUB_OFFLINE"] = "1"

from langgraph.graph import StateGraph,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

class State(TypedDict):
    question: str
    answer: str
    context: str
    need_retrieve: bool

embedder = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")
vectorstore=Chroma(persist_directory="./chroma_multi", embedding_function=embedder)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3",
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    temperature=0.7,
)

def judge_node(state: State):
    keywords=["项目","功能","使用","问题"]
    need_any=any(keyword in state["question"] for keyword in keywords)
    return {"need_retrieve": need_any}

def retrieve_node(state: State):
    docs=retriever.invoke(state["question"])
    context="\n\n".join(d.page_content for d in docs)
    return {"context": context}

def generate_node(state: State):
    ctx=state.get("context","无相关上下文")
    prompt=ChatPromptTemplate.from_template("你是一个知识助手。根据上下文回答问题，不知道就说不知道。\n\n上下文: {context}\n\n问题: {question}")
    chain=prompt | llm | StrOutputParser()
    answer=chain.invoke({"context":ctx,"question":state["question"]})
    return {"answer": answer}

def route_after_node(state: State):
    if state["need_retrieve"]:
        return "retrieve"
    else:
        return "generate"

graph = StateGraph(State)
graph.add_node("judge",judge_node)
graph.add_node("retrieve",retrieve_node)
graph.add_node("generate",generate_node)
graph.set_entry_point("judge")
graph.add_conditional_edges("judge",route_after_node,{"retrieve":"retrieve","generate":"generate"})
graph.add_edge("retrieve","generate")
graph.add_edge("generate",END)
app=graph.compile()

q1="我这个项目是做什么的?"
result =app.invoke({"question": q1})
print(f"问题: {result['question']}")
print(f"回答: {result['answer']}")

q2="Python里字典和列表有什么区别?"
result =app.invoke({"question": q2})
print(f"问题: {result['question']}")
print(f"回答: {result['answer']}")