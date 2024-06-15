ls=eval(input())
ls1=[]
ls2=[]
for i in ls:
    for j in i:
     if j not in ls1:
        ls1.append(j)
ls1.sort()
#print(ls1)
n=len(ls)
count=0
for x in ls1:
    count=0
    for y in ls:
        for z in y:
            if x==z:
             count+=1
    ls2.append(count)
#print(ls2)
n1=len(ls1)
for t in range(n1):
    print(ls1[t],ls2[t],sep=(","))
#统计字符串列表中每个字母出现的次数。
#编写程序，读入一个仅包含字符串对象的列表，然后统计该列表中每个字母出现的次数。
#列表中的字符串对象仅包含小写英文字母。

