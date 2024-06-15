#统计类题目可以考虑用字典保存数据
ls = eval(input())
list = []
for x in ls:
    for y in x:
        list.append(y) #构造含有原ls所有元素的list
list.sort()  #sort()默认按首字母排列                
mydict = {}  #构造一个空字典
for i in list:        
    mydict[i] = mydict.get(i,0) + 1
#get中的i是key,0是value的初值
lst = list(mydict.items()) #items获取字典对象之中的键值对元组，并将字典键值对的数据以列表的形式返回。
for i in range(len(lst)):
    print("%s,%d"%(lst[i][0],lst[i][1]))
    






    
          

            


