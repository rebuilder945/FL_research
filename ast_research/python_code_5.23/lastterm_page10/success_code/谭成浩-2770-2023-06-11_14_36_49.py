a=input()
b=input()
jishu=0
for i in list(a):
    if i in list(b):
        continue
    else:
        jishu+=1
if jishu==0 and len(a)==len(b):
    print('True')
else:
    print('False')
