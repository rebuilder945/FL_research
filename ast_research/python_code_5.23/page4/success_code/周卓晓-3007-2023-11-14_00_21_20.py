a= eval(input())
b=input().split(",")
n=int(b[0])
m=int(b[1])
flag=True
if n>len(a) or m>len(a):
    flag=False
else:
    del a[n:m]
if flag==True:
    print(a)
elif flag==False:
    print("error")



