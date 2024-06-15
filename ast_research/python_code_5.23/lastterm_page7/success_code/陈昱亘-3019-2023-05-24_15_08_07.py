lst=input().split(' ')
keys=['name','english','python','math']
dic=dict(zip(keys,lst))
numlist=list(dic.values())
numlist.remove(dic['name'])
numlist=list(map(int,numlist))
numlist.sort(reverse=True)
dic['avg']=sum(numlist)/3
a,b,c=numlist
print(dic['name'],'%.2f %.2f %.2f %.2f'%(a,b,c,dic['avg']))
