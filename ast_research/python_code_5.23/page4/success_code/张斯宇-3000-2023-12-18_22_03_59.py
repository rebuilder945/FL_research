lst=eval(input())

sum=0
len=len(lst)

for i in range(len):
    sum+=lst[i]

ave=sum/len
print("%.2f" %ave)
