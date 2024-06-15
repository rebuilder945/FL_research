n=eval(input())
n.sort(reverse=False)
b=0
for i in range(len(n)):
    b+=n[i]*10**i
print(b)

