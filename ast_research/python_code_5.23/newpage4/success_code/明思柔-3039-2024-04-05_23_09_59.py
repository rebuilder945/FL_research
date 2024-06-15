a=eval(input())
b=max(a)
c=min(a)
while b in a:#不可以for遍历循环然后删除元素
    a.remove(b)
while c in a:
    a.remove(c)
print(a)
