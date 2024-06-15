a=sorted(list(input()))
b=sorted(list(input()))
c="True"
if len(a)==len(b):
    for x in range(len(a)):
        if a[x] != b[x]:
            m="False"
            break
print(c)
