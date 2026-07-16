from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader

txt_loader=TextLoader('test.txt',encoding='utf-8')
txt_docs=txt_loader.load()
print(f'TXT文档内容：{len(txt_docs)}段')
print(txt_docs[0].page_content[:100])

md_loader=UnstructuredMarkdownLoader("markdown.md")
md_docs=md_loader.load()
print(f"MD文档内容：{len(md_docs)}段")

pdf_loader=PyPDFLoader("test.pdf")
pdf_docs=pdf_loader.load()
print(f"PDF文档内容：{len(pdf_docs)}页")

