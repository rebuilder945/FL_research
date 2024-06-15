def  classify(x,ls):
    lst1=[]
    lst2=[]
    for i in ls:
        if i<=x:
            lst2.append(i)
        elif i>x:
            lst1.append(i)
    dict['k1']=lst1
    dict['k2']=lst2

        

        
x  =  int(input())
ls  =  input().split()
ls  =  list(map(int,ls)) 
dic  =  {}
classify(x,ls)

print(sorted(list(dic.items())))
