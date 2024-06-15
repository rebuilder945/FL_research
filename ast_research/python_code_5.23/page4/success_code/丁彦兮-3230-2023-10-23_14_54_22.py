# n=eval(input())
# sums=range(1,n+1)
# sums2=[]
# m=sums[0]
# for i in range(len(sums)-1):
    # sums2.append(sums[i+1])
# sums2.append(m)
# print(sums2)

# 最大数
a=eval(input())
a.sort(reverse=True)
b=""
for i in range(len(a)):
    b+=str(a[i])
print(int(b))

