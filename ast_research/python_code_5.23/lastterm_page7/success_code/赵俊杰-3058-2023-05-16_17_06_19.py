if __name__=="__main__":
    s= input
    dic={}
    dic[s]=dic.get(s,0)+1
    dicList=[]
    for k,v in dic.items():
        dicList.append([k,v])
    dicList.sort(key=lambda x:x[1],reverse=True)
    ls=dicList[0]
    print("%s %s"%(ls[0],ls[1]))
