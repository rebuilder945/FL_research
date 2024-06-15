n= eval(input())
a,b = eval(input())
a=int(a);b=int(b)
if a<len(n) and b<len(n):
    print("error")
elif a<b:
    del n[a:b]
    print(n)
else:
     print("error")
