a=input()
num1=ord('A')+ord('Z')
num2=ord('a')+ord('z')
for i in a:
    if i.isalpha():
        if i.isupper():
            c=chr(num1-ord(i))
            print(c,end='')
        elif i.lower():
            c=chr(num2-ord(i))
            print(c,end='')
    else:
        print(i,end='')
