n = eval(input())
lst = [x+1 for x in range(n)]
for i in range(n-1):
    lst[i] = lst[i+1]
lst[-1] = 1
print(lst)
