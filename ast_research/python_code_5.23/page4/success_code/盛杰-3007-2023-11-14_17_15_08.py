lst=eval(input())
n,m=eval(input())
if n<len(lst) and m<len(lst):
    a=[]
    for i in range(n):
        a.append(lst[i])
    for j in range(m,len(lst)):
        a.append(lst[j])
    print(a)
else:
    print("error")


