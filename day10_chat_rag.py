import os
os.environ["HF_HUB_OFFLINE"] = "1"

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from operator import itemgetter
from dotenv import load_dotenv
from langchain_chroma import Chroma


load_dotenv()

embedder = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
)

vectorstore = Chroma(
    persist_directory="./chroma_multi",
    embedding_function=embedder,
)

retriever = vectorstore.as_retriever(   
    search_kwargs={"k": 3},
)

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3",
    base_url=os.getenv("SILICONFLOW_BASE_URL"),
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    temperature=0.7,
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识助手。根据上下文回答问题，不知道就说不知道。\n\n上下文: {context}"),
    MessagesPlaceholder(variable_name="history"),
])
chain = (
    {"context": itemgetter("question") | retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)),
     "history": itemgetter("history")}
    | prompt | llm | StrOutputParser()
)

store = {}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

session_id = "user1"
while True:
    question = input("请输入问题: ")
    if question.lower() in ("exit", "quit","q"):
        break
    result = chain_with_history.invoke({"question": question},
                                       config={"configurable":{"session_id": session_id}},
                                       )
    print(f"AI: {result}")
