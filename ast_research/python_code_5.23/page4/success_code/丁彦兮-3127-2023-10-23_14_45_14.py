# n=eval(input=())
# a=range(1,n+1)
# a2=[]
# m=a[0]
# for i in range(len(a)-1):
    # a2.append(a[i+1])
# a2.append(m)
# print(a2)
n=eval(input())
sums=range(1,n+1)
sums2=[]
m=sums[0]
for i in range(len(sums)-1):
    sums2.append(sums[i+1])
sums2.append(m)
print(sums2)

