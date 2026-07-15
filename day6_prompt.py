from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages([
    ("system","你是一个专业的翻译，只输出翻译结果，不需要解释"),
    ("user","把下面的话翻译成{language}:\n{text}"),
])

message=prompt.format(language="英文",text="人工智能正在改变世界")

print(message)
