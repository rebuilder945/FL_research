n=eval(input())
h1=0
for x in range(0,n+1):
      a = []
      if x%2==0:
            a.append(x)
            a1 = sum(a)
            h1 = h1+a1
print(h1)

