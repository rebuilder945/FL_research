n = eval(input())
if n <20 :
    b = 6* (n**2) +1
    print('%.2f'%(b))
elif n >= 40 :
    c = 100 /(n+1)
    print('%.2f'%(c))
else:
    a = (3* n - 60)**0.5
    print('%.2f'%(a)) 
