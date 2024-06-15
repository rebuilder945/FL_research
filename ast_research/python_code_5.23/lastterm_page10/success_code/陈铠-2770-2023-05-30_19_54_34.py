a=input()
b=input()
if a.isalpha() and b.isalpha() and len(a)==len(b):
    if a[0]==b[1]:
        print(True)
    else:
        print(False)
else:
    print(False)
