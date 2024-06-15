lst=list(eval(input()))
n,m=eval(input())
if n <= len(lst):
    lst2 = [lst[n]] * m
    lst.append(lst2)
    print(lst)
else:
    print("error")
