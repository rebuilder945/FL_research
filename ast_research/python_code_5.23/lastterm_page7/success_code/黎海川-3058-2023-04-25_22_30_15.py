def Strcount(s):
    liststr=list(s.split()) 
    strcount={} 
    for i in  liststr: 
        strcount[i]=liststr.count(i)  
    item=[] 
    for k,v in strcount.items():   
        item.append([k,v])          
    item.sort(key=lambda x:x[1],reverse=True)   
    print("")
    a=1
    for i in range(len(item)-1):
        if item[i][1]==item[i+1][1]:
            a=a+1
    for i in range(a):
        print(item[i][0], "", item[i][1])

if __name__=="__main__":
    str = input("\n")
    Strcount(str)


