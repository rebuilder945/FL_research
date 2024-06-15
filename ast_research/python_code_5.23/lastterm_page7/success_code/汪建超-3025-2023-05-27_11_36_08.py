dic = {}
str1 = input().split()
for x in str1 :
    if x in dic :
        dic[x] +=1
    else:
        dic[x] = 1
max_str = max(dic,key= dic.get)
lst = [k for (k,v)in dic.items() if v==dic[max_str]]
for x in lst:
    print(x ,dic[max_str])
