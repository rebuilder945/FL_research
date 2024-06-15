# lst=eval(input())
# lst1=lst.copy()
# for x in lst:
#     if x==0:
#         lst1.remove(0)
#         lst1.append(0)
# print(lst1)

a=eval(input())
b=[]
c=[]
for i in a:
    if i ==0:
        b.append(0)
    else:
        c.append(i)
print(c+b)

