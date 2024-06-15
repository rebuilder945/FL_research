a=input().split()
b=input()
ls=[i for i in a]
for i in ls:
    while i==b:
        ls.remove(i)
print(''.join(ls))
