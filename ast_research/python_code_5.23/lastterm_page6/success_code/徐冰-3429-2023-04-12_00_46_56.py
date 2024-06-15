n=input()
num=0
st=0
sp=0
el=0
for x in n:
    if x.isdigit():
        num=num+1
    elif x.isalpha():
        st=st+1
    elif x.isspace():
        sp=sp+1
    else:
        el=el+1
print(st,sp,num,el)
