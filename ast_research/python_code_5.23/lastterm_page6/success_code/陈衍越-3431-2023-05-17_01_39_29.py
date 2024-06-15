n=int(input())
lst1=['red' if t%2 else 'black' for t in range(1,11)]
lst2=['green']+lst1+lst1[1:9]+lst1+lst1[1:9]
if n>=0 and n<=36:
    print(lst2[n])
else:
    print('error')
