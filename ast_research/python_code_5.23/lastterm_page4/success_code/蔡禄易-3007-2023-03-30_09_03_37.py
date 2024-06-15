lst = input().split(',')
n,m = eval(input())
lst = list(map(int,lst))
if m-1 in len(lst):
    del lst[n:m]
    print(lst)
else:
    print("error")
