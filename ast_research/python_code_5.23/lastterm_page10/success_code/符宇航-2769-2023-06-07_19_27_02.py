mima = list(input())
for i in mima:
    print(i,end='')
mingwen = []
for i in mima:
    if 'a'<=i<='z':
        n=ord('z')-ord(i)+ord('a')
        a=chr(n)
        mingwen.append(a)
    elif 'A'<=i<='Z':
        n=ord('Z')-ord(i)+ord('A')
        a=chr(n)
        mingwen.append(a)
    else:
        mingwen.append(i)
print()
for i in mingwen:
    print(i,end='')



