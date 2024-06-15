n = int(input())
lst = [i for i in range(1, n+1)]
lst = lst[1:] + lst[:1] 
print(lst)
