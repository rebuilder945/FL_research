n=eval(input())
a,b=2,1
list1=[]
for x in range(n):
    e=a
    a+=b
    b=e
    c=a/e
    list1.append(c)
d=sum(list1[0:len(list1)-1])+2
print('%.4f'%d)

