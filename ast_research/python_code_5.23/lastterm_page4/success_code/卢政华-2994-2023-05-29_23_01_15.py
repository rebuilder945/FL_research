lst=eval(input())
n,m=eval(int(input))
if n <len(lst):
    lst2=[lst[n]*m]
    print(lst+lst2)
else:
    print("error")
