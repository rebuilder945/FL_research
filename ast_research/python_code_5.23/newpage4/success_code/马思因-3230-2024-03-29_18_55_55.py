n=eval(input())
n.sort()
s=0
for i in range(len(n)):
    s=n[i]*10**i+s
print(s)
