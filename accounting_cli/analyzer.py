def summary(transactions):
    income=sum(t.amount for t in transactions if t.t_type=="income")
    expense=sum(t.amount for t in transactions if t.t_type=="expense")
    return {"income":income,"expense":expense,"balance":income-expense}

def category_breakdown(transactions):
    result={}
    for t in transactions:
        if t.t_type=="expense":
            result[t.category]=result.get(t.category,0)+t.amount
    return result


