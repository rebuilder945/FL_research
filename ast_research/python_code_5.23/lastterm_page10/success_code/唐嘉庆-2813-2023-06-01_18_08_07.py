a=input().split(' ')
b=input()
while b in a:
    a.remove(b)   
print(' '.join(str(i) for i in a))

    


