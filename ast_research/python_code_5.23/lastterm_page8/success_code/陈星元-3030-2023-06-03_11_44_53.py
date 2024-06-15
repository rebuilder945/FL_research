def match(ls1,ls2):
    ls=[]
    for i in range(len(ls1)):
        str=ls1[i]+" "+ls2[i]
        ls3=str.split()
        ls3[1]=int(ls2[i])
        ls.append(ls3)
    ls.sort(key=lambda x:x[1])
    return ls
ls1=input().split(',')
ls2=input().split(',')
print(match(ls1,ls2))


