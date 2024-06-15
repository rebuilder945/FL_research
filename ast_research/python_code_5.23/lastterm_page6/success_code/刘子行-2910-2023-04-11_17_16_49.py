h=eval(input())
n=eval(input())
s=0
i=1
ass=[]
while i<=n:
    s=h+h/2
    h=h/2
    i+=1
    ass.append(s)
dick=sum(ass)-h
print('%.2f'%dick)
