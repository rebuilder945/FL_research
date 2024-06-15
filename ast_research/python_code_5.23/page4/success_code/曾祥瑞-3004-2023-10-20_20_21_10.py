a=eval(input())
b=[]
for i in a:
    for x in range(1,100):
         if i%x!=0:
            b.append(i)
print(b)
