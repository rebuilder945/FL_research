a=list(input())
b=list(input())
for i in range(len(a)-len(b)+1):
    if b==a[i:i+len(b)]:
        del a[i:i+len(b)]
print(''.join(a))


