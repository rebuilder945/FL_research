keys = input().split(',')
values = list(map(int,input().split(',')))
lst = [[k,v] for k,v in zip(keys, values)]
print(lst)
