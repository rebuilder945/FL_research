s = input()
a,b,c,d = 0,0,0,0
for sb in s:
    if sb.isalpha():
        a += 1
    elif sb.isspace():
        b+=1
    elif sb.isdigit():
        c+=1
    else:
        d+=1
print(a,b,c,d)
