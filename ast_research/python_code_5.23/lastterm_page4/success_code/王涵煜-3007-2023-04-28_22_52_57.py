lst=eval(input())
n,m=eval(input())
if n>m or n<0 or m>len(lst):
    print("error")
else:
    for i in range(n,m):
        lst.pop(n)
    print(lst)

