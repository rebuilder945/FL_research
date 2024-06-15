n=list(input())
ls=[]
for i in n:
    if i.isalpha():
        i=chr(26-(ord(i)-ord('a')+1-1)+ord('a')-1)
        ls.append(i)
    else:
        ls.append(i)
print(''.join(n))
print(''.join(ls))
