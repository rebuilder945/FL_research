from re import I


a="sdffsd123werrer456fgdgdg1dfgdf12"
b=""
c=""
for i in a:
    if i.isnumeric():
        b+=i
    else:
        if len(b)>=len(c):
            c=b
        b=''
print(c)
