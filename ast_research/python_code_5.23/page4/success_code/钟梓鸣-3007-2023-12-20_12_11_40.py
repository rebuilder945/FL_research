a=eval(input())
n,m=eval(input())
if(n>len(a)-1 or n<0 or m>len(a)-1 or m<0):
    print("error")
for i in range(n,m):
    del a[i]
print(a)

