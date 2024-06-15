a = input()
lst = [i for i in a]
a,b,c,d = 0,0,0,0
for i in lst:
    if ord(i)==32:
        b = b+1
    elif ord(i) in range(48,58):
        c = c+1
    elif ord(i) in range(65,91) or ord(i) in range(97,123) :
        a = a+1
    else:
        d = d+1
print(a,b,c,d)
    


