list=eval(input())
n, m=eval(input())
a=[]
if m <= len(list) and n<=m:
    del list[n:m]
    print(list)
else:
    print("error")
