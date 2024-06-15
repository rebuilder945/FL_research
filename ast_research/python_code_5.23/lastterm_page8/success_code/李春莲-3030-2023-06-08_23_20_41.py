n=input().split(',')
g=eval(input())
l=[]
for i in range(len(n)):
    l.append([n[i],g[i]])
l.sort(g,reverse=False)
print(l)
