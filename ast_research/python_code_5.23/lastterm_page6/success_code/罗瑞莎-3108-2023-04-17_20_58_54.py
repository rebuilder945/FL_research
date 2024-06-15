lst = list(input())
lst1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in lst1:
    if lst.count(i)!=0:
        print(i+",%d"%(lst.count(i)))
