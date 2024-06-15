a=input()
b=input()
if a.isalpha() and b.isalpha():
    if a[1]==b[2]:
        print(True)
    else:
        print(False)
else:
    print(False)
