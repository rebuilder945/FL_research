def work(a) :
dic={}
lst = []
for i in range(a+1):
    if i ==0:
        k = 1
    else:
        k *=i
    lst.append((i,k))
dic = dict(lst)
return dic
	

a = int(input())
ans = work(a)
print(ans)

