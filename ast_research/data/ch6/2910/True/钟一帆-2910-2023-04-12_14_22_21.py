h=eval(input())
t=eval(input())
s=h
for i in range(t-1):
        h*=0.5
        s+=2*h
    
print('%.2f'%s)
