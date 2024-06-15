a=eval(input())
b=[]
c=len(a)
for i in a:
    if i!=0:
          b.append(i)
          d=(c-len(b))
    else:
        d=(c-len(b))
print(b+[0]*d)






