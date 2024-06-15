ls1=eval(input())
def f(ls1):
    sum_=sum(ls1)
    num=len(ls1)
    return sum_/num
a=f(ls1)
if a-int(a)==0:
    print(int(a))
else:print("%.2f"%(a))
