n=eval(input())
n.sort(reverse=False)
i=0
b=0
for a in n:
    i+=1
    b+=a*(10**(i-1))
print(b)
