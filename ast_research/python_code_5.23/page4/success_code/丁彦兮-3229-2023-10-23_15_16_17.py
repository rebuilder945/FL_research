# n=eval(input())
# sums=range(1,n+1)
# sums2=[]
# m=sums[0]
# for i in range(len(sums)-1):
    # sums2.append(sums[i+1])
# sums2.append(m)
# print(sums2)

# 最大数
# a=eval(input())
# a.sort(reverse=True)
# b=""
# for i in range(len(a)):
    # b+=str(a[i])
# print(int(b))


# 输出一次(出现的次数)
a=eval(input())
b=[]
for x in a:
    c=a.count(x)
    if c==1:
        b.append(x)
if len(b)==0:
    print("False")
else:
    b.sort(reverse=False)
    b=list(map(str,b))
    print(",".join(b))



