name=input()
a=name.split(",")
nums=input()
nums=nums.strip('[]')
b=nums.split(",")
n=len(a)
ls=[]
for i in range(n):
    a2=a[i]
    b2=eval(b[i])
    s=[a2,b2]
    ls.append(s)
print(ls)

