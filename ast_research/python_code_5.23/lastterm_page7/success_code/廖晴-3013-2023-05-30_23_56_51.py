GDP={}
while True:
        a=input()
        if a=='ok':
                break
        else:
                x,y=map(str,a.split())
                GDP[x]=y
s=[]
for i in GDP.values():
        i=int(i)
        s.append(i)
s.sort()
list1=list(GDP.keys())
list1.sort()
print(list1)
print(s)
print(GDP.get("India","no"))
print(sum(s))
