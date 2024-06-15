a=input()
h=[]
for x in a:
    if x not in '0123456789':
        b=a.replace(x,'*')
ls=b.split('*')
for i in ls:
    if i==" ":
        ls.remove(i)
    else:
        pass
    h.append([i,ls.index(i),len(i)])
    h.sort(key=lambda m:(-m[2],-m[1]))
if h!=[]:
    print(h[0][0])
else:
    print('No digits')



