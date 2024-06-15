s=input()
a=''
b=''
for i in s:
    if i.isdigit():
        a+=i
        if len(a)>=len(b):
            b=a
    else:
        a=''
if len(b)>0:
    print(b) 
else:
    print('No digits')
