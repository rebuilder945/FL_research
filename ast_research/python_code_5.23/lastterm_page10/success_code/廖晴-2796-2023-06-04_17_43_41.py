st=input()
s=list(st)
l=len(s)
a=0
b=0
ss=[]
for x in s:
    if x.isdigit():
        a+=1
if a==0:
    print("No digits")
else:
    print('456')
