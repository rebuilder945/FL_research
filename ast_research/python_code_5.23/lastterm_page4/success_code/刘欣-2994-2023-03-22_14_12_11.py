lst = input().split(",")
lst = [int(i) for i in lst]  
n = int(input())
m = int(input())

if n >= len(lst) or n < -len(lst):
    print("error")
else:
    elem = lst[n]
    lst.extend([elem]*m)
    print(lst)
