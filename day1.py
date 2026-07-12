# name='左惠君'
# age=22
# high=1.73
# is_graduated='已'
# print(f"我叫{name}，{age}岁，身高{high}cm，{is_graduated}毕业")

# name=input("请输入您的姓名：")
# age=input("请输入您的年龄：")
# print(f"你好，{name}，你今年{age}岁")

# a=input("请输入第一个数字：")
# b=input("请输入第二个数字：")
# result=int(a)+int(b)
# print(f"{a}+{b}={result}")

# num_str="123"
# num_int=int(num_str)
# print(num_int+1)

# price_str="19.99"
# price_float=float(price_str)
# print(price_float*2)

# score=95
# print(f"你的成绩是{score}","你的成绩是"+str(score))

# print("年龄："+str(age))


<<<<<<< HEAD
# name=input("请输入您的姓名：")
# age=input("请输入您的年龄：")
# month_money=input("请输入您的月薪：")
# year_money=int(month_money)*12
# high_income=year_money>100000
# print(f"您好，{name}，您今年{age}岁，月薪为{month_money}元，年薪为：{year_money}元,是否高收入：{high_income}")

# 第一个游戏
import random
count=3
answer=random.randint(1,100)
while count>0:
    temp=input("输入一个数字：")
    guess=int(temp)
    if guess==answer:
        print("恭喜你，猜对了")
        print("猜中了也没有奖励")
        break
    else:
        print("猜错了")
    if guess>answer:
        print("大了")
    else:
        print("小了")
    count-=1
print(f"正确答案是：{answer}")
print("游戏结束，不玩了")
=======
name=input("请输入您的姓名：")
age=input("请输入您的年龄：")
month_money=input("请输入您的月薪：")
year_money=int(month_money)*12
high_income=year_money>100000
print(f"您好，{name}，您今年{age}岁，月薪为{month_money}元，年薪为：{year_money}元,是否高收入：{high_income}")
>>>>>>> parent of 40601d3 (day1 :增加了视频学习代码)
