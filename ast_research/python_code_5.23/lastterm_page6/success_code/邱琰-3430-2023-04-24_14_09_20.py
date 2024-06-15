lst1=['12','1','2','3','4','5','6','7','8','9','10','11']
lst2=['spring','summer','autumn','winter']
n=eval(input())
if n not in lst1:
    print('error')
if n in lst1[0,3]:
    print(lst2[3])
if n in lst1[3,6]:
    print(lst2[0])
if n in lst1[6,9]:
    print(lst2[1])
if n in lst1[9,12]:
    print(lst2[2])
