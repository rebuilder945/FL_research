ll=eval(input())
ll.sort(key=int)
sum=0
n=0
for i in ll:
    sum+=i*pow(10,n)
    n+=1
print(sum)

