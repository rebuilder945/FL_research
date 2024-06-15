def jiami(nums):
    lst=list[nums]
    for i in lst:
        lst[i]=(int(lst[i])+5)%10
    for j in range(len(lst)//2):
        lst[j]=lst[-j-1]
        lst[-j-1]=lst[j]
    num=""
    for k in lst:
        num=num+str(k)
    return num
a=input()
b=jiami(a)
print(b)
