str1 = input()
print(str1)
for i in str1:
    if i.islower() :
        i = chr(ord("a")+(ord("z")-ord(i)))
        print(i,end="")
    elif i.isupper():
         i = chr(ord("A")+(ord("Z")-ord(i)))
         print(i,end='')
    else:
        print(i,end="")

