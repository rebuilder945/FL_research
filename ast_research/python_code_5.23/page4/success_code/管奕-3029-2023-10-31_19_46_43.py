name=input() .split(',')
num=eval(input())
a=[]
for x in range(len(name)):
    a.append([name[x],num[x]])
print(a)

