str1 = input()
for i in str1:
    if 'a'<i<'z' or 'A'<i<'Z':
        i = chr(27-ord(i))
        print(i,end="")
    else:
        print(i,end="")

