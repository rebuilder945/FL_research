n=input()
shuzi=""
maxshuzi=""
for i in n:
    if i.isdigit():
        shuzi+=i
        if len(shuzi)>=len(maxshuzi):
            maxshuzi=shuzi
if shuzi!="":
    print(maxshuzi)
else:
    print("No digits")

