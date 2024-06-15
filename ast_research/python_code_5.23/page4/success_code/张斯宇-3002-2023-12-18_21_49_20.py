lst=eval(input())

sum=0
len=len(lst)
for i in range(len):
    sum+=lst[i]

if (sum/len)%1!=0:
    print("%.2f" %(sum/len))
else :
    print("%d" %(sum/len))
