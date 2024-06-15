num=input()
numa=list(num)
for i in range(len(numa)):
    numa[i]=(int(num[i])+5)%10
for j in range(len(numa)//2):
    numa[j],numa[j+1]=numa[-1-j],numa[-j]
str1=""
for k in numa:
    str1=str1+str(k)
str1=int(str1)
print(str1)

