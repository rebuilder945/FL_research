keys = input().split(',')
values = list(map(int,input().split(',')))
lst = [[k,v] for k,v in zip(keys, values)]
lst.sort(key=lambda x:x[1],reverse=False)
print(lst)
