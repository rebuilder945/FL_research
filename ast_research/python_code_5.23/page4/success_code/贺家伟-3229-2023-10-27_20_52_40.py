a=eval(input())
b=[]
for i in range(0,len(a)):
    if a.count(a[i])==1:
        b=b+a[i]
    else:
        print("False")
b.sort()
print(b)
