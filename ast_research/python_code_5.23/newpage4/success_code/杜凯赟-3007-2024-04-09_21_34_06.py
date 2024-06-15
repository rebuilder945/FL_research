from distutils.log import error


lst = [input().split(",")]
a =len(lst)
m = eval(input())
n =list(m)
b = n[0]
c = n[1]
if b<=c:
    for i in range(b,c):
        n.pop(i)
        print(n)
elif b>c:
    for i in range(c,b):
        n.pop(i)
        print(n)
else:
        print("error")
