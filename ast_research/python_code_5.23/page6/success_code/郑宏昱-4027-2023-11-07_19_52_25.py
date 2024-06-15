a,b=0,0
while True:
    n=input()
    if n!="#":
        a+=1
        b=b+int(n)
    else:
        break
print(a,b)
