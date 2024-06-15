a = list(eval(input()))
b = input().split(",")
n = int(b[0])
m = int(b[1])
ls=[]
if n > len(a):
    print("error")
else:
    ls.append(a[n])
    a=a+ls*m
    print(a)


