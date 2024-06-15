a=input()
b=input()
c={x for x in a}
d={y for y in b}
if c==d and len(a)==len(b):
    print('True')
else:
    print('False')
