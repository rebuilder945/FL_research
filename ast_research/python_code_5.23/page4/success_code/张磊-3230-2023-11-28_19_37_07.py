lst=eval(input())
lst.sort(reservse=True)
sum=''
for i in range(len(lst)):
    sum=str(lst[i])+sum
print(int(sum))
