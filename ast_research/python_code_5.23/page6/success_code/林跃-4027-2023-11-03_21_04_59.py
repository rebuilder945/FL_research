m=0
sum=0
while True:
    a=input()
    if a!="#":
        sum=sum+eval(a)
        m=m+1
    else:
        break
print(m,sum)
