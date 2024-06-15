a=eval(input())
lst=a.copy()
n,m=eval(input())
if n>len(a):
    print("error")
else:
    b=a.pop(n)
    x=0
    while x<=m:
        lst.append(b)
        x+=1
print(lst)
