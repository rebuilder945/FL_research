a=eval(input())
b=[]
for i in a:
    if i in range(1,10,2):
        b.append(i)
        if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
            b.append(i)
print(b)
