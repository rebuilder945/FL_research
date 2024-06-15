lt=eval(input())
a=max(lt)
b=min(lt)
jihe=set(lt)#转化为集合去除重复项
for i in jihe:
    if i==a:
        jihe.remove(a)
for i in jihe:
    if i==b:
        jihe.remove(b)
ls=list(jihe)
print(ls)
