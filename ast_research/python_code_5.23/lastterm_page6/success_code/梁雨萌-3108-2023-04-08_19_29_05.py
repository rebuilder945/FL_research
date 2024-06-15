eng=["a","b","c","d","e","f","g","h","i","g","k","l",'m','n','o','p','q','r','s','t','u','v','w','x','y','z']

list1=eval(input())
word=str(list1[0])
list2=[]
for i in range(1,len(list1)):
    word=word+" "+str(list1[i])
    lis=list(word)
for i in eng:
    num=lis.count(i)
    if num!=0:
        a=str(i)+","+str(num)
        list2.append(a)
for i in list2:
    print(i)
