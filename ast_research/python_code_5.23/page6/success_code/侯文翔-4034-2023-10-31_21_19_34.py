from contextlib import redirect_stderr


a=eval(input())
b=eval(input())
m="red"
n="blue"
o="yellow"
if (a==m and b==n) or (a==n and b==m):
    print("purple")
elif (a==o and b==m) or (a==m and b==o):
    print("orange")
elif (a==n and b==o) or (a==o and b==n):
    print("green")
else:
    print("error")
