ls = input()
print(ls)
for i in ls:
    if "A"<=i<="Z":
        print(chr(91-(ord(i)-64)),end="")
    elif "a"<=i<="z":
        print(chr(123-(ord(i)-96)),end="")
    else:
        print(i,end="")
