nums=eval(input())
ls=[]
for x in nums:
    s=nums.count(x)
    if s==1:
        ls.append(x)
    else:
        pass
ls.sort(reverse=False)
if len(ls)==0:
    print("False")
else:
    lista = ','.join(str(i) for i in ls)
    print(lista)
