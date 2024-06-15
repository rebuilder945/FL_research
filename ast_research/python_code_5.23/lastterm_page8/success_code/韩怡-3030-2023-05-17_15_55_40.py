a=input().split(",")
b=list(eval(input()))
c=[]
for x in range(0,len(a)):
    c.append([a[x],b[x]])
def num(t):
    return t[1]
d=sorted(c,key=num)
print(d)

