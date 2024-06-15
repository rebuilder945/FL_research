a=list(input())
b=list(input())
for i in range(len(a)):
    if a[i:]+a[:i]==b:
        print('True')
    else:
        print('else')
