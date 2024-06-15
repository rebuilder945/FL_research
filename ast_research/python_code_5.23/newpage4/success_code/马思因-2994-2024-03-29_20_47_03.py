a=list(eval(input()))
b=list(eval(input()))
if b[0] in range(0,len(a)):
    n=b[0]
    m=b[1]
    c=[a[n]]*m
    print(a+c)
else:
    print("error")

