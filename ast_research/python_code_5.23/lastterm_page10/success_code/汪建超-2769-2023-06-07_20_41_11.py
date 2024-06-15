str1 = input()
print(str1)
for i in str1:
    if 'a'<=i<='z' :
        i = chr(ord("a")+(ord("z")-ord(i)))
        print(i,end="")
    elif 'A'<=i<='z':
         i = chr(ord("A")+(ord("Z")-ord(i)))
    else:
        print(i,end="")

