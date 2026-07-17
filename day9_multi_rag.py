from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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

llm=ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3",
    base_url=os.getenv("SILICONFLOW_API_BASE"),
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    temperature=0.7,
)

txt_loader=TextLoader('test.txt',encoding='utf-8')
txt_docs=txt_loader.load()

md_loader=UnstructuredMarkdownLoader('README.md')
md_docs=md_loader.load()


all_docs=txt_docs+md_docs
all_splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)
all_chunks=all_splitter.split_documents(all_docs)
vectorstore.add_documents(all_chunks)
print(f"添加 {len(all_chunks)} 个文档到向量数据库")

template = """你是一个知识助手，你的任务是根据用户的问题和上下文，生成符合要求的回答。如果上下文不足，就说“我无法回答”。
上下文: {context}
问题: {question}
回答: """
prompt = ChatPromptTemplate.from_template(template)
chain=(
    {"context": retriever | (lambda all_docs: "\n\n".join(d.page_content for d in all_docs)),
     "question": RunnablePassthrough()}
    | prompt | llm | StrOutputParser()
)

question = "我这个项目是做什么的?"
result = chain.invoke(question)
print(f"问题: {question}")
print(f"回答: {result}")