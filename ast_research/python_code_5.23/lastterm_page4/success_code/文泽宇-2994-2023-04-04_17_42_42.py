lst = input().split(",")
n,m = map(int,eval(input()))
lst = [int(i) for i in lst]
if -len(lst)+1 <= n <= len(lst)-1:
    lst += [lst[n]] * m
else:
    print("error")
print(lst)
