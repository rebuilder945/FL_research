ls1=eval(input())
ls2=''.join(ls1)
ls3=[]
ENG=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
for m in ENG:
    if m in ls2:
        if m not in ls3:
            ls3.append(m)
for i in ls3:
    s=ls2.count(i)
    print('%s,%d'%(i,s))
