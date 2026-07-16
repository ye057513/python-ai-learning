## Document 的 page_content 和 metadata
page_content：文档的文本内容
metadata：文档的元数据，如页码、标题等
试text.txt 中的 metadata 里有page字段
## chunk_overlap 为什么不能一刀切
如果chunk_overlap 为0，那么每个chunk 就是文档的一段，这样就丢失了文档的上下文信息。
不重叠会发生什么？重叠20字解决了什么？
不重叠AI会读取出一句断裂的句子，重叠的20字可以连接句子，避免丢失上下文信息。
## chunk_size 太大/太小的坏处
- 100字：每个chunk 骭短，丢失了上下文信息。
- 500字：每个chunk 长，可能包含多个段落。
- 1000字：每个chunk 长，可能包含多个段落。