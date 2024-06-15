a=map(eval,input().split(","))
e=list(a)
b,c=eval(input())
if e[b] in e:
    for i in range(c):
        e.append(e[b])
    print(e)
else:
    print("error")
