str1=input()
ls=[]
strn=''
for i in str1:
    if i.isdigit():
        strn+=i
    else:
        ls.append(strn)
        strn=''
if len(strn)==0:
    print("No digits")
else:
    long=[]
    longest1=[]
    for i in ls:
        long.append(len(i))
    longest=max(long)
    for i in range(len(ls)-1,-1,-1):
        i=str(i)
        if len(i)==longest:
            longest1.append()
    print(longest1[0])
