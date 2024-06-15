a = list(input())
b=[]
for i in a:
    i=eval(i)
    i=(i+5)%10
    b.append(i)
b.reverse()
print(''.join(str(x) for x in b))
