a=0
b=0
while True:
    n=input()
    if n!="#":
        a+=1
        b+=eval(n)
    else:
        break
print(a,b)
