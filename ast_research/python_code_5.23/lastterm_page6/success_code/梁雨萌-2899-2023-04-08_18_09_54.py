n,m=map(int,input().split())
list1=[]
if n<m and n>=0 and m>0 and m<=9:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and a!=c and c!=b and a!=0:
                    word=str(a)+str(b)+str(c)
                    list1.append(word)
    list1.sort()
    word=str(list1[0])
    for i in range(1,len(list1)):
        word=word+" "+str(list1[i])
    print(word)
else:
    print("illegal input")
