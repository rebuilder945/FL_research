lst=list(input())
a0,a1,a2,a3=0,0,0,0
for x in lst:
    if x.isupper() or x.islower():
        a0+=1
    elif x.isspace():
        a1+=1
    elif x.isdigit():
        a2+=1
    else:
        a3+=1
# print('{} {} {} {}'.format(a0,a1,a2,a3))
print(a0,a1,a2,a3)
