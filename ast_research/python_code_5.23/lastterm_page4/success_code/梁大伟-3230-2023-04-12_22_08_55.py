lst=eval(input())
lst.sort(reverse=True)
a=""
for i in lst:
    a=a+str(i)
if a[0]==0:
    print("0")
else:
    print(a)
