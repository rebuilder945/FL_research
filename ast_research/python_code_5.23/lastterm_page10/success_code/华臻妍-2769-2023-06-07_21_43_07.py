def f(x):
    if x in 'qwertyuiopasdfghjklzxcvbnm':
        n=ord('z')-ord(x)+ord('a')
        return chr(n)
    elif x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        n=ord('Z')-ord(x)+ord('A')
        return chr(n)
    else:
        return x
a=input()
print(a)
b=''
for x in a:
    b=b+f(x)
print(b)

