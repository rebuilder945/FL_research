a=eval(input())
b=2/1
c=2
d=1
ad=[b]
for x in range(a-1):
    c1=c+d
    d=c
    r=c1/d
    c=c1
    ad.append(r)
print("%.4f"%(sum(ad)))

