a=map(eval,input().split(","))
e=list(a)
b,c=eval(input())
if -len(e)<=b<=len(e)-1:
    for i in range(c):
        e.append(e[b])
    print(e)
else:
    print("error")
