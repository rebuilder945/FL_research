s = eval(input())
a = 0
b = 0
c = 0
d = 0
for n in s:
    if type(n)==str:
        a+=1
    if type(n)==int:
        b+=1
    if n ==" ":
        c+=1
    else:
        d+=1
print(a,c,b,d)





                    




