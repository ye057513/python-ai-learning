import os
os.environ["HF_HUB_OFFLINE"] = "1"
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import math
from datetime import datetime

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3",
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    temperature=0.7,
)
class State(TypedDict):
      messages: Annotated[list, add_messages]

@tool
def search_knowledge(keyword: str) -> str:
      """当用户询问项目、代码、文件、文档相关内容时，调用此工具检索本地知识库。"""
      return f"搜索「{keyword}」：找到 3 条相关结果：(1) ... (2) ... (3) ..."

@tool
def calculate(expression: str) -> str:
      """当用户询问计算相关问题时，调用此工具进行计算。"""
      try:
            result = eval(expression, {"__builtins__": {}}, {"math": math})
            return f"计算结果：{expression} = {result}" 
      except Exception as e:
            return f"计算错误：{str(e)}"

@tool
def get_current_time() -> str:
      """当用户询问时间相关问题时，调用此工具获取当前时间。"""
      return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tools = [search_knowledge, calculate, get_current_time]
llm_with_tools = llm.bind_tools(tools)

def route(state: State) -> str:
    """检查最后一条消息是否有 tool_calls，决定是去 tools 节点还是结束。"""
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    else:
        return "end"

def chatbot(state: State) -> State:
    """根据用户输入，调用工具或生成回复。"""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages":[response]}

tool_node = ToolNode(tools)
graph = StateGraph(State)
graph.add_node("agent", chatbot)
graph.add_node("tools", tool_node)
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", route, {"tools": "tools", "end": END})
graph.add_edge("tools", "agent")
app = graph.compile()



messages = [HumanMessage(content="搜索 LangGraph？")]
result = app.invoke({"messages": messages})
print("==结果==")
for message in result["messages"]:
      print(f"[{message.type}] {message.content}")
