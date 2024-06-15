n=int(input())
a=2.0
b=1.0
tatal=0
for i in range(n):
    total=total+a/b
    a,b=a+b,a
print(f'{total:.4f}')
