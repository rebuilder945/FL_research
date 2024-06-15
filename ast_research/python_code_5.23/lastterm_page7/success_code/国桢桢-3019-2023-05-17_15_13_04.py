a = input().split()
b=a[1::]
for i in range (len(b)):
    b[i]=float(b[i])
c = sum(b)/len(b)
d = max(b)
e = min(b)
b.remove(d)
b.remove(e)
f = b[0]
print(a[0],"%.2f"%(d),"%.2f"%(e),"%.2f"%(f),"%.2f"%(c))
