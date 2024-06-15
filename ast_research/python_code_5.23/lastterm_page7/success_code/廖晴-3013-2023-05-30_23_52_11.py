GDP={}
while True:
        a=input()
        if a=='ok':
                break
        else:
                x,y=map(str,a.split())
                GDP[x]=y
s=map(int,list(GDP.values()))
print(list(GDP.keys()))
print(s)
print(GDP.get("India","no"))
print(sum(s))
