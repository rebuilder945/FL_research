lst=eval(input())
n,m=eval(input())
if n < len(lst) and m < len(lst):
    for i in range(n,m):
        lst.pop(i)
        print(lst)
else:
    print("error")
