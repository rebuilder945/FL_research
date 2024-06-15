lst = eval(input())
lst1 = []
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
if lst1:
    lst1.sort()#join函数，连接字符串作为连接符
    print((",").join(str(i) for i in lst1))#join函数后是字符串，因此意为需要将列表中的整数转变成字符串
else:
    print(False)
