a=input()
h=[]
for x in a:
    if x not in '0123456789':
        a=a.replace(x,'*')
        c=a.split('*')
        for i in c:
            if i==' ':
                c.remove(i)
                h.append([i,c.index(i),len(i)])
                h.sort(key=lambda m:(-m[2],-m[1]))
                if h!=[]:
                    print(h[0][0])
                else:
                    print('No digits')



