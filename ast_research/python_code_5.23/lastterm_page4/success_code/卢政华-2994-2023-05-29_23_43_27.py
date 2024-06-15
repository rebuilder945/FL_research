lst=list(eval(input()))
n,m=eval(input())
if n <= len(lst):
    lst2 = [lst[n-1]] * m
    lst.append(lst2)
    print(lst)
else:
    print("error")
