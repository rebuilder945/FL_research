a = input()
lst = [x for x in a]
a,b,c,d = 0,0,0,0
for x in lst:
    if ord(x)==32:
        b = b+1
    elif ord(x) in range(48,58):
        c = c+1
    elif ord(x) in range(65,91) or ord(x) in range(97,123) :
        a = a+1
    else:
        d = d+1
print(a,b,c,d)
    
