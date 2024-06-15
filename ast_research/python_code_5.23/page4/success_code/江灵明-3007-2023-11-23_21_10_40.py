n= eval(input())
a,b = eval(input())
if a<len(n) or b<len(n):
    print("error")
elif a<b:
    del n[a:b]
    print(n)
else:
     print("error")
