ls= input().split()
lis=[]
for x in ls:
    a=ls.count(x)
    ls.append(x)
for i in ls:
    if ls.count(i)==max(lis):
        print(i,max(lis))
        break
