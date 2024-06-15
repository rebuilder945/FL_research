def Strcount(s):
    liststr=list(s.split())  #得到每个字符串，保存为列表
    strcount={} #创建一个空字典
    for i in  liststr: #遍历list中的字符串
        strcount[i]=liststr.count(i)   #统计出现的字符串个数，并写入字典strcount
    # print(strcount)
    item=[] #创建一个空列表
    for k,v in strcount.items():    #遍历strcount中的键值对
        item.append([k,v])          #将遍历出来的键值对添加到item这个列表
    item.sort(key=lambda x:x[1],reverse=True)   #对item列表以出现次数从高到低排序
    #如果出现相同的，就都打印出来
    a=1
    for i in range(len(item)-1):
        if item[i][1]==item[i+1][1]:
            a=a+1
    for i in range(a):
        print(item[i][0], "出现次数：", item[i][1])

if __name__=="__main__":
    str = input()
    Strcount(str)
