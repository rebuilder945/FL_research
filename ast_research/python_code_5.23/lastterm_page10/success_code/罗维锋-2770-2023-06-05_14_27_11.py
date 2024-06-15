a=sorted(list(input()))
b=sorted(list(input()))
c="True"
if len(a)==len(b):
    for x in range(len(a)):
        if a[x] != b[x]:
            c="False"
            break
else:
    c="False"
print(c)
