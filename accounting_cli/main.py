from transaction import Transaction
from storage import load_data,save_data
from analyzer import summary,category_breakdown

def add_transaction(transactions):
    try:
        amount=float(input("请输入金额："))
        category=input("请输入分类：")
        note=input("请输入备注：")
        t_type=input("请输入交易类型(1=income,2=expense)：")

        if t_type=="1":
            t_type="income"
        elif t_type=="2":
            t_type="expense"
        else:
            print("无效的交易类型")
            return
        
        t=Transaction(note,amount,category,t_type)
        transactions.append(t)
        save_data(transactions)
        print(f"已记录:{t}")
    except ValueError:
        print("请输入有效的金额")

def show_summary(transactions):
    s=summary(transactions)
    print(f"\n==汇总==")
    print(f"总收入：{s['income']:.2f}")
    print(f"总支出：{s['expense']:.2f}")
    print(f"总余额：{s['balance']:.2f}")

    breakdown=category_breakdown(transactions)
    if breakdown:
        print(f"\n==支出分类==")
        for cat,amount in breakdown.items():
            print(f"{cat}: ￥{amount:.2f}")

def show_history(transactions):
    if not transactions:
        print("暂无交易记录")
        return
    print(f"\n==交易记录{len(transactions)}笔==")
    for i,t in enumerate(transactions,1):
        sign="+" if t.t_type=="income" else "-"
        print(f"{i}.[{t.date}]{sign}￥{t.amount:.2f}|{t.category}|{t.note}")

def main():
    transactions=load_data()
    print("===个人记账工具===\n")

    while True:
        print("\n1.添加交易")
        print("2.查看汇总")
        print("3.查看交易记录")
        print("4.退出")
        choice=input("请输入您的选择：")
        if choice=="1":
            add_transaction(transactions)
        elif choice=="2":
            show_summary(transactions)
        elif choice=="3":
            show_history(transactions)
        elif choice=="4":
            print("谢谢使用！")
            break
        else:
            print("无效的选择")
            continue

if __name__=="__main__":
    main()

    
    
    