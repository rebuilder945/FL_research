n=eval(input())
s=list(''.join(n))
ls=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in ls:
    if i in s:
        ls1=[i,str(s.count(i))]
        print(','.join(ls1))
