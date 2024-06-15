def findstr(n="None"):
    dic={}
    lst=[]
    for i in n:
        dic[i]=dic.get(i,0)+1
    print(dic)
    for k,v in dic.items():
        lst.append([k,v])
    for i in range(len(lst)):
        if lst[i][1]==1:
            print(lst[i][0])
            break

    
a="helloworldhahaha!"
findstr(a)
        
    
