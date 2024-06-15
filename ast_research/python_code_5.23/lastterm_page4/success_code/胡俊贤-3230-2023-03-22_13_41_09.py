ls=eval(input())
ls.sort(reverse=True)
new=[]
for i in ls:
    j=str(i)
    new.append(j)
s=''.join(new)
if s[0] in '0':
    print("0")
else:
    print(s)

