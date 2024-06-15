a=int(input())
b=int(input())
sums=a
for x in range(b-1):
    sums+=a*(0.5)**(x)
print(sums)
