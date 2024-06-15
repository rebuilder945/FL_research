a=input().split()
b=list(map(int,input().split()))
l=[]
for i in range(len(a)-1):
    ll=[]
    ll.append(a[i])
    ll.append(b[i])
    l.append(ll)
print(l)
