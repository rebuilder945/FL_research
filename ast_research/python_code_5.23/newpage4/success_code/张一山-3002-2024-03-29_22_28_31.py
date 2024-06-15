M=eval(input())
A=sum(M)/len(M)
if A-round(A)==0:
    print('%d'%A)
else:
    print('%.2f'%A)
