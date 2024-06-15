keys = input().split(',')
values = eval(input())
lst = [[a,b] for a,b in sorted(zip(keys,values),key=lambda x:x[1])]
print(lst)
