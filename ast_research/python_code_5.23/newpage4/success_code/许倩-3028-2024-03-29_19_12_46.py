# 第七题
# names=input().split(",")
# scores=eval(input())
# a=[]
# for x in range(len(names)):
#     a.append([names[x],scores[x]])
# print(a)

# 第八题
n,m,l=map(int,input().split(','))
array=[n]
for i in range(m-1):
    n=n-1
    array.append(n)
print(array)
