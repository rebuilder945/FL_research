t=input()
t=t.replace("[","").replace("]","")
t=t.split(',')
t=list(map(int,t))
n,m=eval(input())
if n<=m and m+1<=len(t):
    for i in t[n:m]:
        t.remove(i)
    print(t)
else:
    print("error")







