lst = input().split()
dic = {}
for i in lst:
    dic[i] = dic.get(i,0)+1
lst1 = list(dic.items())
lst1.sort(key=lambda x:x[1],reverse=True)
max1 = lst1[0][1]
lst1.sort(key=lambda x:x[0])
for j in lst1:
    if j[1] == max1:
        print(j[0],j[1])
