a=input()
b=input()
c="True"
for x in a:
    if x not in b:
        m="False"
        break
if len(a)!=len(b):
    c="False"
print(c)
