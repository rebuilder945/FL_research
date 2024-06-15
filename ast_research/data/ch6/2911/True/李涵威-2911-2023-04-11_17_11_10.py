num = input()
s = []
for i in num:
    i = (int(i)+5)%10
    s.append(i) 
if len(s) == 2:
    s[0],s[-1] = s[-1],s[0]
elif len(s) > 2:
    s[0],s[-1] = s[-1],s[0]
    s[1],s[-2] = s[-2],s[1]
print(*s,sep="")
