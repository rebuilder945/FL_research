list1=list(eval(input()))
N=0
W=0
B=0
E=0
for i in list1:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        W+=1
    elif ord(i)>=48 and ord(i)<=57:
        N+=1
    elif i==" ":
        B+=1
    else:
        E+=1
print("{} {} {} {}".format(W,B,N,E))
