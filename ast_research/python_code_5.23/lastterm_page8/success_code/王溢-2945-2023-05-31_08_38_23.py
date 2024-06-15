def add_id(data2):
    list1=[]
    for x in data2:
      a="20"+x
      list1.append(a)
    return list1

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

