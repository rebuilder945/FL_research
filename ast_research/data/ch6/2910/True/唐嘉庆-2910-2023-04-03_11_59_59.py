a=eval(input())
n=eval(input())
c=[]
for i in range(n):
   d=2*a*((0.5)**(i)) 
   c.append(d)
e=sum(c)-a
print('%.2f'%(e))
