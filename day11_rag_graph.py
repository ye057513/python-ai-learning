import os
os.environ["HF_HUB_OFFLINE"] = "1"

from typing import TypedDict
from langgraph.graph import StateGraph,END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    question: str
    answer: str
    context: str

embedder = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")
vectorstore = Chroma(persist_directory="./chroma_multi", embedding_function=embedder)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3",
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    temperature=0.7,
)
def retrieve_node(state: State):
    docs=retriever.invoke(state["question"])
    context="\n\n".join(d.page_content for d in docs)
    return {"context": context}

def generate_node(state: State):
    prompt=ChatPromptTemplate.from_template("你是一个知识助手。根据上下文回答问题，不知道就说不知道。\n\n上下文: {context}\n\n问题: {question}")
    chain=prompt | llm | StrOutputParser()
    answer=chain.invoke({"context":state["context"],"question":state["question"]})
    return {"answer": answer}

graph = StateGraph(State)
graph.add_node("retrieve",retrieve_node)
graph.add_node("generate",generate_node)
graph.set_entry_point("retrieve")
graph.add_edge("retrieve","generate")
graph.add_edge("generate",END)
app=graph.compile()

result =app.invoke({"question": "我这个项目是做什么的?"})
print(f"问题: {result['question']}")
print(f"回答: {result['answer']}")
