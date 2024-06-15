from audioop import lin2adpcm


a=int(input())
b=int(input())
l1=0
for i in range(b):
    if i==0:
        l2=a
    elif i>0:
        l2=a*(0.5**i)*2
    l1=l1+l2
print("%.2f"%l1)
