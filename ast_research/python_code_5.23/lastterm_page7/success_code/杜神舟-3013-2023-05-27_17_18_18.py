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
ls1.sort()
ls2.sort()
print(ls1)
print(ls2)
if dic.get("India","no")=='no':
    print('no')
else:
    print('yes')
print(sum(ls2))
