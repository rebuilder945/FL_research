a=input()
for i in a:
    if i.isalpha():
        print(chr(2*ord(a)+26-ord(i)),end="")
    else:
        print(i,end="")
