def bianhuan(x):
    la = [chr(ord('a')+i) for i in range(26)]
    lb = la[-1::-1]
    if ord(x) in range(97,123) or ord(x) in range(65,91):
        if ord(x) in range(97,123):
            i = la.index(x)
            a = lb[i]
        else:
            i = la.index(x.lower())
            a = lb[i].upper()
    else:
            a = x
    return str(a)
mi = input()
lm = list(mi)
s = ''
for x in lm:
    s = s+bianhuan(x)
print(mi)
print(s)
    

   

