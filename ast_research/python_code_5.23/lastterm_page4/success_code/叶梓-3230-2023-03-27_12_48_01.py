ls=eval(input())
ls.sort()
ls.reverse()
text=''
for i in ls:
    append=str(i)
    text=text+append
if int(text)==0:
    print(0)
else:
    print(text)
