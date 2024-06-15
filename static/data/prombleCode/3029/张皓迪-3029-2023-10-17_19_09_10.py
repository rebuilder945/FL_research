name=list(input().split(','))
grade=eval(input())
ls=[]
for i in range(0,len(name),1):
    a=name[i]
    b=grade[i]
    c=[a,b]
    ls.append(c)
print(ls)
