n=str(input())
c=""
for x in n:
    a=(int(x)+5)%10
    a=str(a)
    c=c+a
b=[i for i in c]


b.reverse()
print("".join(b))

