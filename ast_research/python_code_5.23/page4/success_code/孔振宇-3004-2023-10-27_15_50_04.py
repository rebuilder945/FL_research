a=eval(input())

b=[]
for i in a:
    if i==2 or i==3 or i==5 or i==7 or (i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%9!=0 and i!=1):
            b.insert(-1,i)
            b.sort()
print(b)


