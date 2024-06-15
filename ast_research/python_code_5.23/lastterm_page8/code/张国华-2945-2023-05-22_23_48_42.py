def add_id(data2):
          result=[]
            for i in range(len(data2)):
                if len(data2[i])==6 and data2[i].startswith('20'):
                    result.append('20'+data2[i])
                else:
                    result.append(data2[i])
            return result

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

