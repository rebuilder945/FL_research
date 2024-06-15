n=input()
ls=[]
longest=[]
for i in range (len(n)):
    if "0"<=s[i]<="9":
        ls.append(s[i])
        if len(ls)>=len(longest):
            longest=ls.copy(
    else:
        ls=[]

if len(longest)>0:
    print("".join(longest))
else:
    print('No digits')



