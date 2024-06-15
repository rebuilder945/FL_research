l1=[chr(ord('A')+x)for x in range(26)]
l2=[chr(ord('a')+x)for x in range(26)]
ls=[]
n=list(input())
for x in n:
    if ord(x) in range(65,91):
        i=l1.index(x)
        x=l1[25-i]
        ls.append(x)
    elif ord(x) in range(97,123):
        i=l2.index(x)
        x=l2[25-i]
        ls.append(x)
    else:
        ls.append(x)
print(''.join(n))
print(''.join(ls))



      
