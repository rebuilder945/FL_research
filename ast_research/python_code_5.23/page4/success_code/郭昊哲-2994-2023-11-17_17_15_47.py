a=list(eval(input()))
b,c=eval(input())
if b>=len(a):
    print("error")
else:
    f=a[b]
    for i in range(c):
        a.append(f)
    print(a)


    








