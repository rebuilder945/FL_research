n=eval(input())
m=eval(input())
ll=set('red','blue','yellow')
l=set(m,n)
if n not in ll or m not in ll or m==n:
    print("error")
else:
    if ll-l==('red'):
        print('green')
    elif ll-l==('yellow'):
        print('purple')
    elif ll-l==('blue'):
        print('orange')


