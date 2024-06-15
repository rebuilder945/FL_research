list0 = eval(input())
list1 = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(len(list0)):
    for j in range(len(list0[i])):
        for k in range(len(list2)):
            if list0[i][j] == list2[k]:
                list1[k] = list1[k] + 1
for i in range(len(list1)-1,-1,-1):
    if list1[i] == 0:
        list1.pop(i)
        list2.pop(i)
for i in range(len(list1)):
    print(list2[i],list1[i],sep=",")
