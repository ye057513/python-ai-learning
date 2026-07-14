#类与异步
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def introduce(self):
         print(f"我是 {self.name}，我今年 {self.age} 岁")
    
    #创建一个学生对象
s1=Student("张三",18)
s2=Student("李四",19)

s1.introduce()
s2.introduce()
#父类继承
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

pets=[Dog("旺财"),Cat("小白"),Dog("来福")]
for pet in pets:
    print(f"{pet.name} ：{pet.speak()}")

# @dataclass —— 懒人必备
class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def __ref__(self):
        return f"Student(name={self.name},age={self.age},score={self.score})"
    
from dataclasses import dataclass

@dataclass
class Student:
    name:str
    age:int
    score:float
s=Student("张三",18,90.5)
print(s)
# 自测

class LLMClient:
    def __init__(self,model_name,api_key):
        self.model_name=model_name
        self.api_key=api_key
        self.call_count=0
    def chat(self,message):
        self.call_count+=1
        return f"模型 {self.model_name} 回复：{message}"
    def get_stats(self):
        return {"Model":self.model_name,"调用次数":self.call_count}

client=LLMClient("gpt-4","sk-1234567890abcdef1234567890abcdef")
print(client.chat("你好"))
print(client.chat("今天天气不错！！"))
print(client.get_stats())
#异步编辑
import time

def sync_call():
    print("调用API-1...")
    time.sleep(2)
    print("API-1返回")
    print("调用API-2...")
    time.sleep(2)
    print("API-2返回")
    print("调用API-3...")
    time.sleep(2)
    print("API-3返回")
start=time.time()
sync_call()
print(f"同步耗时:{time.time()-start:.1f}秒")

import asyncio
import time

async def async_call(name):
    print(f"调用{name}...")
    await asyncio.sleep(2)
    print(f"{name}返回")

async def main():
    await asyncio.gather(
        async_call("API-1"),
        async_call("API-2"),
        async_call("API-3")
        )
start=time.time()
asyncio.run(main())
print(f"异步耗时:{time.time()-start:.1f}秒")

# asyncio语法规则
import asyncio

# 异步函数
async def fetch_data(url):
    print(f"请求{url}...")
    await asyncio.sleep(1)
    return f"数据{url}"

# await只能在async内使用
async def process():
    result=await fetch_data("https://www.baidu.com")
    print(result)

# 用asyncio.run()运行异步函数
asyncio.run(process())

# 可以使用asyncio.gather()并行运行多个异步函数
async def main():
    results=await asyncio.gather(
        fetch_data("https://www.baidu.com"),
        fetch_data("https://www.taobao.com"),
        fetch_data("https://www.jd.com")
        )
    print(results)

asyncio.run(main())

# 模拟真实场景

import asyncio
import random

async def call_llm(model,message):
    delay=random.uniform(0.5,2.0)
    await asyncio.sleep(delay)
    return f"[{model}]{message} →回复：耗时{delay:.1f}秒"

async def compare_models(prompt):
    results=await asyncio.gather(
        call_llm("gpt-4",prompt),
        call_llm("Marvis",prompt),
        call_llm("Deepseek",prompt)
        )
    for r in results:
        print(r)

asyncio.run(compare_models("你好"))


