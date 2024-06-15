def add_id(data2):
    lst = []
    for x in data2:
          if len(x) == 6:
                lst.append("20" + x)
          else:
                lst.append(x)
        return lst

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

