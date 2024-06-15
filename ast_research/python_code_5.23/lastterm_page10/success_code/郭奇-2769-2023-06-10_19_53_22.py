yuan=list(input())
lst1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst3=[]
for i in range(len(yuan)):
    if yuan[i].isalpha():
        if yuan[i].supper():
            yuan[i]=lst2[26-i]
            lst3.append(yuan[i])
        else:
            yuan[i]=lst1[26-i]
            lst3.append(yuan[i])
    else:
            lst3.append(yuan[i])
print(''.join(yuan[0:]))
print(''.join(lst3[0:]))
        

