M=eval(input())
M1=[]
for x in range(len(M)):
    if M.count(M[x])==1:
        M1.append(M[x])
M1.sort()
if len(M1)==0:
    print("False")
else:
    print(",".join(map(str,M1)))
