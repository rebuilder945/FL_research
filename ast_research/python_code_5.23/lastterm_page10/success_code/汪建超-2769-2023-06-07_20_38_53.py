str1 = input()
print(str1)
for i in str1:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        i = chr(ord("a")+(ord("z")-ord(i)))
        print(i,end="")
    else:
        print(i,end="")

