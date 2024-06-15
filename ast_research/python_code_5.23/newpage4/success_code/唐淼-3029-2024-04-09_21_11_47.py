a=[input()]
b=input()
for i in range(len(a)):
    c=[[x+y for x in a[i] for y in b[i]]]
print(c)
