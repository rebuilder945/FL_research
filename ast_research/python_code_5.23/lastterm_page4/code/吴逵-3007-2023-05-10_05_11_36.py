lst = eval(input())
n, m = map(int, input().split())
if n > m or n < 1 or m > len(lst):
print("error")
else:
del lst[n-1:m-1]
print(lst)
