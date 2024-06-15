n=eval(input())
lst=[]
for x in range(n+1):
    y=str(x)
    if len(y)==3:
        s=int(y[0])**3+int(y[1])**3+int(y[2])**3
        if s==x:
            print(x)
            lst.append(x)
if len(lst)==0:
    print("none")
