a=list(eval(input()))
a.sort()
s=[]
for i in a:
    if a.count(i)==1:
        s.append(i)
    else:
        pass
if s:
    for i in s[:-1]:

        print(i,end=",")
        print(s[-1])

else:
    print("False")
