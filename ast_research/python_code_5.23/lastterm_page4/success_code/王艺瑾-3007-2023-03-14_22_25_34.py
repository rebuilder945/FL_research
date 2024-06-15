a=eval(input())
b=eval(input())
c=b[0]
d=b[1]
if c in range(len(a)) and d in range(len(a)):
    del a[c:d]
    print(a)
else:
    print("error")
