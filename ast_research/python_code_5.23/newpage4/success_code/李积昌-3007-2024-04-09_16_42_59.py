a= eval(input())
b,c = eval(input())
if b <=len(a) and c<=len(a):
    print(a[:b]+a[c:])
else:
    print("error")
