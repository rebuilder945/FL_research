n=input()
shuzi=""
maxshuzi=""

for i in n:
    if i.isdigit():
        shuzi+=i
    elif shuzi!="":
        if len(shuzi)>=len(maxshuzi):
            maxshuzi=shuzi
            shuzi=""
if maxshuzi!="":
    print(maxshuzi)
else:
    print("No digits")

