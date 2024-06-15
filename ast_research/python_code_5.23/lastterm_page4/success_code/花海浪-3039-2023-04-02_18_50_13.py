# a=eval(input())
# b=sum(a)
# c=b/(len(a))
# if type(c)==float:
#     print('%.2f'%c)
# else:
#     print(int(c))
a=eval(input())
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=max(b)
d=min(b)
b.remove(c)
b.remove(d)
print(b)

    
