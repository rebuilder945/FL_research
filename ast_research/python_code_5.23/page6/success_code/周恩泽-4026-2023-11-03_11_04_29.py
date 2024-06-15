n=eval(input())
a=1
b=2
c=[1,2]
d=[]
for x in range(n-1):
    x=c[-1]+c[-2]
    c.append(x)
# print(c)
for i in range(1,len(c)):
    x=c[i]/c[i-1]
    d.append(x)
# print(d)
m=sum(d)
print("%.4f"%m)
# n1=[2/1,3/2,5/3,8/5,13/8,21/13]
# n2=0
# n3=eval(input())
# for x in range(n3):
#     n2=n2+n1[x]



# print("%.4f"%n2)
