a=input()
dic={}
ls=[]
ls2=[]
i=0
while True:
    if a=='q':
        break
    else:
        dic[a]=dic.get(a,0)+1
        i+=1
        a=input()
for x,y in dic.items():
    ls.append(y)
    ls2.append(x)
for x,y in dic.items():
    if y==max(ls):
        print(x,y)


