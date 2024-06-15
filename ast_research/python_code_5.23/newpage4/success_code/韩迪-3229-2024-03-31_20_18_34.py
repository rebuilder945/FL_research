a=list(eval(input()))
a.sort()
s=[]
for i in a:
    if a.count(i)==1:
        s.append(i)
    else:
        pass
# if len(s)>1:
#     for i in s[:-1]:

#         print(i,end=",")
#         print(s[-1])
if len(s)==1:
    print(s[0])

if len(s)==0:
    print("False")
else:
    for i in s[:-1]:

        print(i,end=",")
    print(s[-1])
