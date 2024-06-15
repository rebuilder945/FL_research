keys = input().split(',')
values = list(map(int,input().split(',')))
lst = [[k,v] for k,v in zip(keys, values)]
lst.reverse()
print(lst)
