str1=input().strip()
list1=eval(str1)
Sum=0
for i in range(0,len(list1)):
    Sum+=list1[i]
aver=Sum/len(list1)
i_aver=int(aver)
if aver-i_aver==0:
    print(i_aver)
else:
    output=format(aver,".2f")
    print(output)

