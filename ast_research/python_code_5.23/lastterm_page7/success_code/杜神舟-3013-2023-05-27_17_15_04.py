a=input()
ls1=[]
ls2=[]
dic={}
while True:
    if a=='ok':
        break
    else:
        
        x,y=a.split()
        dic[x]=int(y)
        ls1.append(x)
        ls2.append(int(y))
        a=input()
print(ls1)
print(ls2)
print(dic.get("India","no"))
print(sum(ls2))
