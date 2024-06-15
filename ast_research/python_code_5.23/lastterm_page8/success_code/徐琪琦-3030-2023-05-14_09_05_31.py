namelist = input().split(",")
scorelist = input().split(",")
dic = {}
for i in range(len(namelist)):
    dic[namelist[i]] = eval(scorelist[i])
lst = list(dic.items())
lst = sorted(lst,key = lambda x:x[1])  #注意sorted的返回值是list,注意转为list再用lambda函数
lst = list(map(list,lst))          #外面如果不加list就会输出map object at..
print(lst)


