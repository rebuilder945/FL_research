a = list(eval(input()))
b,c = eval(input())
if b<0 or b>=len(a):
    print("error")
else:
    d = [a[b]]*c
    a = a+d
    print(a)
