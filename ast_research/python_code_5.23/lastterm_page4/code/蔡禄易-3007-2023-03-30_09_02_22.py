lst = input().split(',')
n,m = eval(input())
lst = list(map(int,lst))
if m-1 in len(lst):
    print(del(lst[n:m]))
else:
    print("error")
