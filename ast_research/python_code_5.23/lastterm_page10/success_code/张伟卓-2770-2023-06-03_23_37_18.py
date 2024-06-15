a=input()
b=input()
jishu=0
for i in a:
    if i in b:
        continue
    else:
        jishu+=1
if jishu==0 and len(a)==len(b):
    print("True")
else:
    print("False")


