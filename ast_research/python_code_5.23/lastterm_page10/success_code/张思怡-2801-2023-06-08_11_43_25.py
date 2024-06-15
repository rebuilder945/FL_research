a=input()
b=[0,0,0,0,0]

for char in a:
    if '0'<= char <='9':
        b[0]=1
    if 'a'<= char <='z':
        b[1]=1
    if 'A'<= char <='Z':
        b[2]=1
    if len(a)>=8:
        b[3]=1
    if  char.isdigit():
        b[4]=1
print(sum(b))
