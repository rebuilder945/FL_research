a=list(eval(input()))
b,c=eval(input())
if b in range(len(a)):
    d=[a[b]]*c
    print(a+d)
else:
    print("Error")

