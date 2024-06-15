l=eval(input())
n,m=eval(input())
if n>len(l)-1 or n<-len(l):
    print("error")
del l[n]
while m>0:
    l.append(n)
    m-=1
print(l)
