a=input()
b=[0,0,0,0,0]

for char in a:
    if '0'<= char <='9':
        b[0]=1
    elif 'a'<= char <='z':
        b[1]=1
    elif 'A'<= char <='Z':
        b[2]=1
    else:
        b[4]=1
if len(a)>=8:
    b[3]=1
print(b)
print(sum(b))
