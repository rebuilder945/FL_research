a=input()
b=input()
i=0
for x in a:
    if x in b:
        i=i+1
if i ==len(a)==len(b):
    print('True')
else:
    print('False')
