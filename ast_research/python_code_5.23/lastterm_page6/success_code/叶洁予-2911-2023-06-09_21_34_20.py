def jiami(num):
    lst=list[num]
    for i in range(len(lst)):
        lst[i]=(int(lst[i])+5)%10
    for j in range(len(lst)//2):
        lst[j]=lst[-j-1]
        lst[-j-1]=lst[j]
    str1=""
    for k in lst:
        str1=str1+str(k)
    return str1
num=input()
str1=jiami(num)
print(str1)
