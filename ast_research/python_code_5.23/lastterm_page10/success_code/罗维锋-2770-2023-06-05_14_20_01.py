a=input().sort()
b=input().sort()
c="True"
if len(a)==len(b):
    for x in range(len(a)):
        if a[x] != b[x]:
            m="False"
            break
print(c)
