lower='abcdefghijklmnopqrstuvwxyz'
lowerreversed=lower[::-1]
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upperreversed=upper[::-1]

code=input()
codesolved=''
for x in code:
    if x.islower():
        num=lower.find(x)
        codesolved+=lowerreversed[num]
    elif x.isupper():
        num=upper.find(x)
        codesolved+=upperreversed[num]
    else:
        codesolved+=x
print(code)
print(codesolved)
