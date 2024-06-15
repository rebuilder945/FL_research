lst=eval(input())
n,m=eval(input())
a=len(lst)-1
if n<=a and m<=a:
    print(lst[0:n]+lst[m:])
elif n>a or m>a:
    print("error")
