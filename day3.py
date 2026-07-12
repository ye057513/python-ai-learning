#函数
def great():
    print("Hello, World!")

great()

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("张三")

def add(a, b):
    return a + b

result = add(5, 3)
print(f"结果是： {result}")

def order_coffee(size="中杯",suger=True):
    suger_text = "加糖" if suger else "不加糖"
    print(f"{size}, {suger_text}")
order_coffee()
order_coffee("大杯")
order_coffee(suger=False)

def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4, 5))
print(total_sum(1, 2, 3))

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
print_info(name="张三", age=18, sex="男")

def api_call(url, *args, **kwargs):
    print(f"调用API: {url}")
    print(f"参数: {args}")
    print(f"关键字参数: {kwargs}")
api_call("https://api.example.com", "v1", "users",method="GET",TOKEN="ABC123")

# 自测

def calc_salary(base,*bonuses,**deductions):
    money=base+sum(bonuses)-sum(deductions.values())
    return money

result=calc_salary(5000,1000,500,tax=300,insurance=200)
print(f"工资是： {result}")
#异常处理
# num=input("请输入一个数字：")
# result=100/int(num)
# print(result)

# try:
#     num=input("请输入一个数字：")
#     result=100/int(num)
#     print(result)
# except ValueError:
#     print("请输入数字，而不是字母")
# except ZeroDivisionError:
#     print("除数不能为0")

def call_ai_api(prompt,retry=3):
    for i in range(retry):
        try:
            #模型调用
            import random
            if random.random()<0.6:
                raise ConnectionError("网络连接超时")
            return f"AI回答: {prompt}"
        except ConnectionError as e:
            print(f"第{i+1}次尝试失败：{e}")
            if i==retry-1:
                return "抱歉，服务暂不可用"
        except Exception as e:
            print(f"发生未知错误：{e}")
            return "抱歉，发生未知错误" 
response=call_ai_api("请帮我写一首诗")
print(response)   