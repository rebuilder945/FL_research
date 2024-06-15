keys = input().split(',')
values = eval(input())
lst = [[k,v] for k,v in sorted(zip(keys,values),key=lambda x:x[1])]
print(lst)
