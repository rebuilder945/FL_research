n=input()
lst=[i for i in n]
u=''
c=0
for x in n:
    if x.isdigit():
        u+=x
        c+=1
    else:
        u+=' '
if c == 0 :
    print('No digits')
else:
    changdu=[]
    cao=[]
    niubi=u.split()
    for d in niubi:
        changdu.append(len(d))
    for s in niubi:
        if len(s)==max(changdu):
            cao.append(s)
    print(cao[-1])

