min=input()
xiao=(ord('a')+ord('z'))
da=(ord('A')+ord('Z'))
print(min)
for x in min:
    if 'a'<=x<='z':
        print(chr(xiao-ord(x)),end='')
    elif 'A'<=x<='Z':
        print(chr(da-ord(x)),end='')
    else:
        print(x,end='')
