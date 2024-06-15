a=list(eval(input()))
b=list(eval(input()))
n=b[0]
m=b[1]
if b[0] in range(0,len(a)) or n in range(-1,-len(a)-1):
    c=[a[n]]*m
    print(a+c)
else:
    print("error")

