def work(a) :
if a <0:
    dic={0:1}
    return dic
x=1
dic={0:1}
for i in range(a):
    x*=i+1
    dic[i+1]=x
return dic
	

a = int(input())
ans = work(a)
print(ans)

