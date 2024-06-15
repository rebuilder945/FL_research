a=eval(input())
d,c=eval(input())
if d<=c or c>len(a)+1:
    print("error")
else :
    del a[d:c]
print(a)
