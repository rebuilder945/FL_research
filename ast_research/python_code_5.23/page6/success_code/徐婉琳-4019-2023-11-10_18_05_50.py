b=input()
c=list(b)
n=[]
for x in c:
    f=int(x)
    d=(f+5)%10

    n.append(d)
n[0],n[-1]=n[-1],n[0]
n[1],n[-2]=n[-2],n[1]
print(*n,sep=(""))#这个*可以将列表中的数字元素转化为数字


