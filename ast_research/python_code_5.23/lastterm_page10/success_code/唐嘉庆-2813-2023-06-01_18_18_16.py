a=input().split(' ')
b=input()
while b in a:
    c=a.index(b)
    a.remove(b)   
    a.insert(c,'')
print(' '.join(str(i) for i in a))

    


