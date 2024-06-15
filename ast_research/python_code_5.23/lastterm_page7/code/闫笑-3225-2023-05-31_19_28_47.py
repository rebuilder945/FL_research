def work(a) :
n= 0
s = 1
dic ={}
while n <=a:
    lst=[n,s]
    dic[lst[0]] = lst[1]
    n+=1
    s = n*s
return dic
	

a = int(input())
ans = work(a)
print(ans)

