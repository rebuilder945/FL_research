# num=list(input())
# lst=[]
# sum=0
# for i in num:
#     i=int(i)
#     i=(i+5)%10
#     lst.append(i)
# lst[0],lst[-1]=lst[-1],lst[0]
# lst[1],lst[-2]=lst[-2],lst[1]
# for j in range(0,len(lst)):
#     sum+=lst[j]*10**(len(lst)-j-1)
# print(sum)

 
a=input()
temp=str()
for i in a:
    temp=str((int(i)+5)%10)+temp
print(temp)    
