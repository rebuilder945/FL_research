def encrypt(num):
    numa=list(num)
    for i in range(len(numa)):
        numa[i]=(int(num[i])+5)%10
    for j in range (len(numa)//2):
        numa[j],numa[-1-j],numa[j]
    str1=""
    for k in numa:
        str1=str1+str(k)
    return str1
num=input()
str1=encrypt(num)
print(str1)

