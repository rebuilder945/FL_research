a=input()
for x in a:
    if x.isalpha():
        a=a.replace(x," ")
b=a.split()
d=0
max=0
for x in b:
    c=len(x)
    if c>=d:
        d=c
        max=x
if max==0:
    print("No digits")
else:
    print(max)
