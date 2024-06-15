str1 = input()
a = 0
b =0
c =0
d =0
for i in str1[0:len(str1)]:
    if i ==' ':
        b += 1
    elif ord('a')<=ord(i) <=ord('z'):
        a += 1
    elif ord('0') <=ord(i)<=ord('9'):
        c += 1
    else:
        d +=1 
print(a,b,c,d)

