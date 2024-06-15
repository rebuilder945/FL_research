h = eval(input())
n = eval(input())
a = 1
ls =[h]
while a<=n-1:
    h=h/2
    ls.append(h)
    ls.append(h)
    
    a = a+1
b = sum(ls)
print('%.2f'%b)
