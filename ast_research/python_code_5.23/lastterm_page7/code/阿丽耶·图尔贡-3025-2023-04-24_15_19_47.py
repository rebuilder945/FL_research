def Strcount(s):
    liststr=list(s.split())
    strcount={}
    for i in liststr:
        strcount[i]=liststr.count(i)
        print(strcount)
        item=[]
        for k,v in strcount.items():
            item.append([k,v])
        item.sort(key=lembda x:x[1],reverse=Ture)
        print("出现次数最多的单词：")
            a=1
        for i in range(len(item)-1):
            if item[i][1]==item[i+1][1]:
                a=a+1
        for i in range(a):
            print(item[i][0],"出现次数:",item[i][1])
if _name_=="_main_":
    str=input("请输入任意数量的字符串，用逗号隔开\n")
    strcount(str)


