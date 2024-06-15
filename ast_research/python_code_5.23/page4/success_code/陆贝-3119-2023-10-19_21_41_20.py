ls=eval(input())
lt=[]
for i in ls[::-1]:#题目要求是保留最后一个，我写成了保留第一个
    if i not in lt:
        lt.insert(0,i)
print(lt)#多写几个列表来方便处理
