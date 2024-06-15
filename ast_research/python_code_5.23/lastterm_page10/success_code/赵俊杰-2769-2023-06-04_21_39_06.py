str1=input()
print(str1)
str2=list(str1)
for x in str2:
    if x.isalpha():
        if x.islower():
            print(chr(25+97*2-ord(x)),end="")
        else:
            print(chr(25+65*2-ord(x)),end="")
    else:
        print(x,end="")
