a = input().split()
b=a[1::]
b.reverse()
for i in range (len(b)):
    b[i]=float(b[i])
c = sum(b)/len(b)
print(a[0],"%.2f"%(b[0]),"%.2f"%(b[1]),"%.2f"%(b[2]),"%.2f"%(c))
