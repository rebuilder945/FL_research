a=input()
b=input()
if a.isalpha() and b.isalpha() and len(a)==len(b):
    if a[0]==b[1] and a[1]==b[0]:
        print(True)
    else:
        print(False)
else:
    print(False)
