name=input().split(',')
grade=eval(input())
out=[]
for i in range(len(name)):
    out.append([name[i],grade[i]])
print(out)    
