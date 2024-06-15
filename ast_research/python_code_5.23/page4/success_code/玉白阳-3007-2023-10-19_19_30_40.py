ls1=eval(input())
n,m=eval(input())
if m in range(len(ls1)) and n in range(len(ls1)):
    del ls1[n:m]
else:
    print("error")
