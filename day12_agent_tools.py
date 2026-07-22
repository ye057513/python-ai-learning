import os
os.environ["HF_HUB_OFFLINE"] = "1"

from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
      messages: Annotated[list[BaseMessage], add_messages]

embedder = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5",)
vectorstore = Chroma(persist_directory="./chroma_multi", embedding_function=embedder)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

@tool
def search_knowledge(question: str) -> str:
      """当用户询问项目、代码、文件、文档相关内容时，调用此工具检索本地知识库。"""
      docs = retriever.invoke(question)
      return "\n\n".join(d.page_content for d in docs)

tools = [search_knowledge]
tools_by_name = {t.name: t for t in tools}

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3",
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    temperature=0.7,
)
llm_with_tools =llm.bind_tools(tools)

def agent_node(state: State):
      response = llm_with_tools.invoke(state["messages"])
      return {"messages":[response]}

def tool_node(state: State):
      last_message = state["messages"][-1]
      result = []
      for tc in last_message.tool_calls:
            t=tools_by_name[tc["name"]]
            output=t.invoke(tc["args"])
            result.append(ToolMessage(content=output, tool_call_id=tc["id"]))
      return {"messages": result}

def should_continue(state: State) -> Literal["tools", "__end__"]:
      last_message = state["messages"][-1]
      if last_message.tool_calls:
            return "tools"
      else:
            return "__end__"

graph = StateGraph(State)
graph.add_node("agent", agent_node)
graph.add_node("tool", tool_node)
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue, {"tools": "tool", "__end__": END})
graph.add_edge("tool", "agent")
app = graph.compile()

messages = [HumanMessage(content="我这个项目是做什么的？")]
result = app.invoke({"messages": messages})
print("==结果==")
for message in result["messages"]:
      print(f"[{message.type}] {message.content}")
