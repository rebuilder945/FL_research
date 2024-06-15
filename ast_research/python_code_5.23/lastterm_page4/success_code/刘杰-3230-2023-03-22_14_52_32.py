list=eval(input())
list.sort(reverse=True)
sum=''
for i in range(len(list)):
    sum+=str(list[i])
print(int(sum))
