lst=eval(input()).split("")
list1 = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
list2 = list(range(0,10))
list7 = [ ]
list3 = []
list4 = []
list5 = []
list6 = []
for x in lst:
    if x in list1:
        list3.append(x)
    elif x in list2:
        list4.append(x)
    elif x in list7:
        list5.append(x)
    else:
        list6.append(x)
print(len(list3),len(list4),len(list5),len(list6))

