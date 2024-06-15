a=input()
c=list(a.split(","))
b=eval(input())
h=[]
for i in range(len(b)):
    j=[c[i],b[i]]
    h.append(j)
print(h)
    

