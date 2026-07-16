from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader=TextLoader('test.txt',encoding='utf-8')
docs=loader.load()

configs=[
    {"name":"细粒度","size":100,"overlap":20},
    {"name":"中等","size":500,"overlap":50},
    {"name":"粗粒度","size":1000,"overlap":100},
]

for cfg in configs:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=cfg['size'],
        chunk_overlap=cfg['overlap']
    )
    chunks = splitter.split_documents(docs)

    print(f"\n===== {cfg['name']} | size={cfg['size']} overlap={cfg['overlap']} =====")
    print(f"总段数: {len(chunks)}段")
    print(f"第一段字符数: {len(chunks[0].page_content)}")
    print(f"最后一段字符数: {len(chunks[-1].page_content)}")
    print(f"第一段预览: {chunks[0].page_content[:50]}")


