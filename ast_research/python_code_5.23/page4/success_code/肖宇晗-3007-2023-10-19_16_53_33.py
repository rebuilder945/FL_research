lst = input()
n,m = eval(input())
if n>len(lst)-2 or m>len(lst):
    print("error")
else:
    if n<=m:
        del lst[n,m]
        print(lst)
    else:
        print("error")
    

