name=input().split(',')
name=list(name)
grade=eval(input())
m=[]
for x in range(len(name)):
    n=[]
    n.append(name[x],grade[x])
    m.append(n)
    print(m)
