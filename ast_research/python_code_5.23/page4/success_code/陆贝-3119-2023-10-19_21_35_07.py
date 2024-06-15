ls=eval(input())
lt=[]
for i in ls[0:0:1]:
    if i not in lt:
        lt.append(i) 
print(lt)#多写几个列表来方便处理
