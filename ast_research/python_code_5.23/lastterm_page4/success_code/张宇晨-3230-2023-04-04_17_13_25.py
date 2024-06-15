lst=eval(input())
lst.sort(reverse=True)  #从大到小排序，降序
sum=''  #留个空填东西
for i in range(len(lst)):
    sum+=str(lst[i])  #列表转换成字符串，字符串拼接
print(int(sum))  #字符串转换成整数
