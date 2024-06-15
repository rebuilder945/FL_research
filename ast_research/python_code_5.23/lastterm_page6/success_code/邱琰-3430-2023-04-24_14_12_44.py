lst2=['spring','summer','autumn','winter']
n=eval(input())
if n<=0 or n>=13:
    print('error')
if n==12 or n==1 or n==2:
    print(lst2[3])
if n>=3 and n<=5:
    print(lst2[0])
if n>=6 and n<=8:
    print(lst2[1])
if n>=9 and n<=11:
    print(lst2[2])
