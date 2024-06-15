l=eval(input())
l.sort(reverse=True)
sum=''
for i in range(len(l)):
    sum+=str(l[i])
if sum!=0:
    print(sum)
else:    
    print("0")


