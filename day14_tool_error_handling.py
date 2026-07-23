import os
os.environ["HF_HUB_OFFLINE"] = "1"
from dotenv import load_dotenv
load_dotenv()

# TODO 1: 导入必要的模块
# 提示：与 Day13 完全相同

# TODO 2: 配置 ChatOpenAI（model=deepseek-ai/DeepSeek-V3）
# 提示：base_url=os.getenv("SILICONFLOW_BASE_URL")

# TODO 3: 定义 State TypedDict
# 提示：messages: Annotated[list, add_messages]

# ===== 工具定义 =====
# TODO 4: 定义 search_knowledge 工具（同 Day13）
# @tool
# def search_knowledge(keyword: str) -> str:
#     """当用户询问项目、代码、文件、文档相关内容时，调用此工具检索本地知识库。"""
#     return ...

# TODO 5: 定义 calculate 工具（关键变化！）
# ⚠️ 与 Day13 的区别：不要用 try/except 捕获异常
# 让 eval 的异常直接向外抛出，LangGraph 会自动生成
# status="error" 的 ToolMessage 并传给 LLM
# @tool
# def calculate(expression: str) -> str:
#     """当用户询问计算相关问题时，调用此工具进行计算。"""
#     result = eval(expression, {"__builtins__": {}}, {"math": math})
#     return f"计算结果：{expression} = {result}"

# TODO 6: 定义 get_current_time 工具（同 Day13）

# ===== 图构建 =====
# TODO 7: tools = [...]
# TODO 8: llm_with_tools = llm.bind_tools(tools)
# TODO 9: 定义 route 函数（同 Day13）
# TODO 10: 定义 chatbot(state) 函数（同 Day13，必须包一层）
# TODO 11: tool_node = ToolNode(tools)
# TODO 12: 构建 graph（agent → route → tools/END → agent）

# ===== 测试 =====
# TODO 13: 正常调用测试
# messages = [HumanMessage(content="计算 100 + 200")]
# result = app.invoke({"messages": messages})
# 打印每条消息的 [type] content

# TODO 14: 错误场景测试
# messages = [HumanMessage(content="计算 1 / 0 等于多少")]
# result = app.invoke({"messages": messages})
# 观察 LLM 收到的 ToolMessage 是否包含 status="error"
# 观察 LLM 如何向用户解释错误
