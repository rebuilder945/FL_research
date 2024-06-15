n=input()
shuzi=""
maxshuzi=""
flag=False
for i in n:
    if i.isdigit():
        shuzi+=i
        flag=True
    else:
        if flag:    
            if len(shuzi)>=len(maxshuzi):
                maxshuzi=shuzi
            shuzi=""
            flag=False
if maxshuzi:
    print(maxshuzi)
else:
    print("No digits")

