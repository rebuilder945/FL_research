a=input()
b='abcdefghijklmnopqrstuvwxyz'
for x in a:
    if x.isalpha():
        i=b.index(x)+1
        print(b[26-i],end='')
    else:
        print(x,end='')

