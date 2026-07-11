#数组
sorces=[85, 90, 78, 92, 88]
print("The scores are:", sorces[0])
print(sorces[-1])
print(sorces[0:3])

sorces.append(95)
sorces.insert(2, 80)
sorces.remove(78)
sorces[0]=66
print(sorces)

result=[]
for i in range(10):
    result.append(i*2)
print(result)

result1=[i*2 for i in range(10)]
print(result1)

result2=[x for x in range(10) if x%2==0]
print(result2)

names=["张三","李四","王五"]
greetings=[f"你好，{name}" for name in names]
print(greetings)

#自测
nums = [3, 7, 12, 5, 9, 20, 1]
answers=[i*i for i in nums if i>5]
print(answers)

student={"name": "张三", "age": 22, "score": 92.5,"is_graduated": True}

print(student["name"])
print(student.get("height", "未填写"))

student["score"]=95
student["phone"]=12345678901

for key, value in student.items():
    print(f"{key}: {value}")
#     分三步理解
# 第一步：student.items() 返回什么
# python
# student = {"name": "张三", "age": 22, "score": 92.5}

# print(student.items())
# # 输出：dict_items([('name', '张三'), ('age', 22), ('score', 92.5)])
# 相当于把字典拆成一个个小包裹（元组），每个包裹里装着 (键, 值)：

# 包裹1: ('name', '张三')
# 包裹2: ('age', 22)
# 包裹3: ('score', 92.5)
# 第二步：for ... in ... 逐个取出
# python
# for 变量 in 一堆东西:
#     # 每次循环，变量 = 下一个包裹
# 第一次循环：变量 = ('name', '张三') 第二次循环：变量 = ('age', 22) 第三次循环：变量 = ('score', 92.5)

# 第三步：key, value 是拆包裹
# Python 允许同时用两个变量接住元组，自动拆开：

# python
# 包裹 = ('name', '张三')
# key, value = 包裹

# # 相当于：
# key = 包裹[0]    # 'name'
# value = 包裹[1]  # '张三'
# 完整对照
# python
# student = {"name": "张三", "age": 22}

# for key, value in student.items():
#     print(f"{key}: {value}")
# 循环走了两轮，等价于手动写：

# python
# # 第1轮
# key, value = ('name', '张三')
# print(f"{key}: {value}")   # name: 张三

# # 第2轮
# key, value = ('age', 22)
# print(f"{key}: {value}")   # age: 22

users={"user1": {"name": "张三", "score": 88},
       "user2": {"name": "李四", "score": 90},
       "user3": {"name": "王五", "score": 95}}

print(users["user2"]["name"])
print(users["user2"]["score"])

passed=[info["name"] for uid, info in users.items() if info["score"]>=90]
print(passed)

a={"x":1, "y":2}
b={"y":3, "z":4}
merged=a|b
print(merged)

orders=[{"product":"键盘", "price": 299, "quantity": 2},
        {"product":"鼠标", "price": 199, "quantity": 1},
        {"product":"显示器", "price": 499, "quantity": 1},
        {"product":"鼠标垫", "price": 29, "quantity": 5}]
total=sum(order["price"]*order["quantity"] for order in orders)
print(f"订单总金额为：{total}")

expenses=[order["product"] for order in orders if order["price"]>300]
print(f"高成本商品有：{expenses}")

order_sorted=sorted(orders, key=lambda x: x["price"]*x["quantity"], reverse=True)
# 1️⃣ Lambda 表达式（匿名函数） ✅ 当前写法

# python
# # 适合：简单、一次性的排序规则
# sorted(orders, key=lambda x: x["price"]*x["quantity"])
# 2️⃣ 普通函数（命名函数）

# python
# def get_order_total(order):
#     return order["price"] * order["quantity"]

# order_sorted = sorted(orders, key=get_order_total)
# 适用场景：逻辑复杂或需要复用时

# 3️⃣ 内置函数/方法

# python
# # 按字符串长度排序
# words = ["apple", "banana", "cherry"]
# sorted(words, key=len)  # 结果: ['apple', 'banana', 'cherry']

# # 按字典某个键的值排序
# sorted(orders, key=lambda x: x["price"])  # 只按单价排
# 4️⃣ operator 模块（更高效）

# python
# from operator import itemgetter, attrgetter

# # 按字典的 "price" 键排序（等价于 lambda x: x["price"]）
# sorted(orders, key=itemgetter("price"))

# # 按对象的属性排序
# # sorted(objects, key=attrgetter("name"))
# 5️⃣ 类方法 / 静态方法

# python
# class OrderSorter:
#     @staticmethod
#     def by_total(order):
#         return order["price"] * order["quantity"]

# sorted(orders, key=OrderSorter.by_total)
for order in order_sorted:
    print(f"{order['product']}：{order['price']}X{order['quantity']}={order['price']*order['quantity']}元")
    