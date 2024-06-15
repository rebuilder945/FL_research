def depart(str):
    dic={}
    ls=[]
    for i in str:
        ls.append(i)
    for i in ls:
        dic[i]=dic.get(i,0)+1
    return dic
str1=input()
str2=input()
if len(str1)==len(str2):
    if depart(str1)==depart(str2):
        print(True)
    else:
        print(False)
else:
    print(False)
