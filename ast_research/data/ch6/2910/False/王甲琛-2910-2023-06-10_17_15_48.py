high=eval(input())
n=eval(input())
lst=[high]
for i in range(n):
    high=high/2
    lst.append(high*2)
print("%.2f"%(sum(lst)))
