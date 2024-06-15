c = eval(input())
a,b =eval(input())
if a>len(c) or b>len(c):
    print("error")
else:
    for i in range(a,b+1):
        c.pop(i)
    print(c)
