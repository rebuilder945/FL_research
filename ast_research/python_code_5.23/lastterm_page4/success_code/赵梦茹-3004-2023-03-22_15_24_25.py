def prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
             return False
        else:
            return True
    else:
        return False
st1=list(eval(input()))
st2=[]
for k in st1:
    if prime(k)==True:
        st2.append(k)
print(st2)
