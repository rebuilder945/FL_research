def add_id(data2):
    ids=[]
    for id in data2:
      ids.append('20'+id)
    return ids
      

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

