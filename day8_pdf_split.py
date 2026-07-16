from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_loader=PyPDFLoader("test.pdf")
pdf_docs=pdf_loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20,
)
chunks = splitter.split_documents(pdf_docs)
for chunk in chunks:
    print(chunk.metadata)
    print(chunk.page_content[:100])
    print("\n")

pages=set(chunk.metadata.get("page") for chunk in chunks)
print(f"\n总页数: {len(chunks)}")
print(f"涉及页码: {sorted(pages)}")



