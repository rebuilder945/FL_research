dic = {}
str1 = input().split()
for x in str1 :
    if x in dic :
        dic[x] +=1
    else:
        dic[x] = 1
print(dic)
