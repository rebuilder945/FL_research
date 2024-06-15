a=input()
print(a)
b=[]
for i in a:
    if 'a'<=i<='m':
        i=chr(ord(i)+2*(ord('m')-ord(i))+1)
        b.append(i)
    elif 'A'<=i<='M':
        i=chr(ord(i)+2*(ord('M')-ord(i))+1)
        b.append(i)        
    elif 'n'<=i<='z':
        i=chr(ord(i)-2*(ord(i)-ord('n'))-1)
        b.append(i)
    elif 'N'<=i<='Z':
        i=chr(ord(i)-2*(ord(i)-ord('N'))-1)
        b.append(i)        
    else:
        b.append(i)
print(''.join(b))
    


