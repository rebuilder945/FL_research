a=eval(input())
d,c=eval(input())
if c<=d or c>len(a)+1:
    print("error")
else :
    del a[d:c]
    print(a)
