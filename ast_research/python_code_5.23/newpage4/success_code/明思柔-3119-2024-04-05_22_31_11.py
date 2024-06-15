a=eval(input())
b=[]
a.reverse()#这道题的关键点
for i in a:
    if i not in b:
        b.append(i)
print(b)
