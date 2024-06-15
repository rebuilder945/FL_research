def work(a) :
d={}
for i in range(a+1):
    d[i]=jc(i)
return d
def jc(b):
    s=1
    for t in range(1,b+1):
        s=s*t
    return s
	

a = int(input())
ans = work(a)
print(ans)

