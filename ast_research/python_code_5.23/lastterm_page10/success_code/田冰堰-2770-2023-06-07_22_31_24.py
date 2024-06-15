a=input()
b=input()
for i in a:
    if a[i:]+a[:i]==b:
        print('True')
    else:
        print('else')
