i=eval(input())
p=0
for x in i:
    p+=x
n=p/len(i)
u=int(n)
if n-u>0:
    print('%.2f'%n)
else:
    print(u)


