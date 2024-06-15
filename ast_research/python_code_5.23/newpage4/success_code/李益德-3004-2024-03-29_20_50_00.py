list_1 =list(eval(input()))
list_2 =[]
for i in list_1:
    a=0
    for r in range(i):
        if i%(r+1)==0 :
            if not i ==(r+1) and not (r+1) ==1:
                a+=1               
    if a ==0 and i!=0 and i!=1:
        list_2.append(i)
print(list_2)


        
