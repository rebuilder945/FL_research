a=input()
s1="abcdefghijklmnopqrstuvwxyz"
s2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ls1=(x for x in s1)
ls2=(x for x in s2)
for j in a:
    if j.isalpha():
        if j in s1 :
                m=s1.find(j)
                print(s1[25-m],end="")
        if j in s2:
                m=s2.find(j)
                print(s2[25-m],end="")
    else:
        print(j,end="")
