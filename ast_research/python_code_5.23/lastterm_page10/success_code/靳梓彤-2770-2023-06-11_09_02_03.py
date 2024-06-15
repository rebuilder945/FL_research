word1=input()
word2=input()
if len(word1)==len(word2):
    lst1=[]
    lst2=[]
    for i in word1:
        lst1.append(i)
    for i in word2:
        lst2.append(i)
    lst11=lst1.sort()
    lst22=lst2.sort()
    if lst11!=lst22:
        print("False")
    elif lst11==lst22:
        print("True")
elif len(word1)!=len(word2):
    print("False")


