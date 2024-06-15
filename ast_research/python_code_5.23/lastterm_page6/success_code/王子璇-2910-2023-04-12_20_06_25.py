h=eval(input())
N=eval(input())
lst=[h]
for i in range(N-1):
    h=0.5*h
    lst.append(h*2)
a=sum(lst)
print('%.2f'%a)
