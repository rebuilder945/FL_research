nums=eval(input())
list=[]
for x in nums:
    if nums.count(x)>1:
        pass
    else:
        list.append(x)
if len(list)==0:
    print("False")
elif len(list)>0:
    list.sort()
    lista = ','.join(str(i) for i in list)
    print(lista)



   


