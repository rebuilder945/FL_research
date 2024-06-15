def work(a) :
dic1={0:1}
x=1
for i in range(1,a+1):
    for j in range(1,i+1):
        x*=j
    dic1[i]=x
    x=1
return dic1

	

a = int(input())
ans = work(a)
print(ans)

