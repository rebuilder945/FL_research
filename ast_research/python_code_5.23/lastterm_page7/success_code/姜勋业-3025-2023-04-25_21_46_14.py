def classify(x,ls):
    ls1=[]
    ls2=[]
    for i in ls:
        if i>x:
            ls1.append(i)
        else:
            ls2.append(i)
        dic['k1']=ls1
        dic['k2']=ls2
x=int(input())
ls=input().split()
ls=list(map(int,ls))  
dic={}
classify(x,ls)
print(sorted(list(dic.items())))
