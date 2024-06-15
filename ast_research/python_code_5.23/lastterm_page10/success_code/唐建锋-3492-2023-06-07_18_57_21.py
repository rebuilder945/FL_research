def first(str):
    dic={}
    for i in range(len(str)):
        if str[i] in dic:
            dic[str[i]]+=1
        else:
            dic[str[i]]=1
    for i in range(len(str)):
        if dic[str[i]]==1:
            return str[i]
str1=input()
print(first(str1))

