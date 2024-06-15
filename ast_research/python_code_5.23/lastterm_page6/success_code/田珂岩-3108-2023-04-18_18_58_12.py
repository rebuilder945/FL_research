#统计类题目可以考虑用字典保存数据
s = eval(input())
ls = []
for x in s:
    for y in x:
        ls.append(y) #构造含有原ls所有元素的list
ls.sort()  #sort()默认按首字母排列                
mydict = {}  #构造一个空字典
for i in ls:        
    mydict[i] = mydict.get(i,0) + 1
#get中的i是key,0是value的初值
lst = list(mydict.items()) #items获取字典对象之中的键值对元组tuple，并将字典键值对的数据以列表的形式返回。
for i in range(len(lst)):
    print("{names},{times}".format(names = lst[i][0],times = lst[i][1]))
    #print("%s,%d"%(lst[i][0],lst[i][1]))
    
    







    
          

            


