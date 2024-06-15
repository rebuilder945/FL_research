A=input()
n,m=eval(input())
if n<=len(A)+1 and m<=len(A)+1:
    if n<=m:
       B=A[0:n]
       C=A[m:]
       D=[B,C]
       print(D)
    elif n>m:
        E=A[0:m]
        F=A[n:]
        G=[E,F]
        print[G]
else:
   print('error')
    
    
