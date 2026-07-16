from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader=TextLoader('test.txt',encoding='utf-8')
docs=loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
)

chunks=splitter.split_documents(docs)
print(f"原文1段,切分后{len(chunks)}段")
print(f"第一段前100个字符：{chunks[0].page_content[:100]}")
print(f"第一段元数据：{chunks[0].metadata}")
