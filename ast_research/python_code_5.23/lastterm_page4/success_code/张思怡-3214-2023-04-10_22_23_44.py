a=eval(input())
b=[]
for i in a:
    if i!=0:
        b.append(i)
# print(b)
c=[0]*(a.count(0))
print(b+c)
