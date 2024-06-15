k=""
b=[]
while k!="#":
    k=input()
    if k!="#":
        b.append(k)
print(len(b),sum(list(map(int,b))))

