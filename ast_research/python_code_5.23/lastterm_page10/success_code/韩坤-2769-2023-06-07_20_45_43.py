n=input()
n1=""
lst1=[chr(i) for i in range(97,123)] #小写
lst2=[chr(i) for i in range(65,91)]  #大写
for x in n:
    if x.isalpha():
        if x.isupper():
            a=lst2.index(x)
            x=lst2[25-a]
            n1=n1+x
        else:
            a=lst1.index(x)
            x=lst1[25-a]
            n1=n1+x
    else:
        n1=n1+x
print(n)
print(n1)
