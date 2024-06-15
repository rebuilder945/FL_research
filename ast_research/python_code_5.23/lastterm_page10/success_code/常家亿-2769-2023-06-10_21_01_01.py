a=input()
lst1=[chr(x) for x in range(65,91)]
lst2=[chr(t)for t in range(97,123)]
print(a)
if a.isalpha:
    for x in a:
        if x in lst1:
            i=lst1.index(x)
            a=a.replace(x,lst1[25-i])
        elif x in lst2:
            j = lst2.index(x)
            a=a.replace(x,lst2[25-j])
    print(a)
