word1=input()
word2=input()
lst=[]
if word1.isalpha() and word2.isalpha():
    lst1=[]
    lst2=[]
    for i in word1:
        lst1.append(i)
    for i in word2:
        lst2.append(i)
    lst11=lst1.sort()
    lst22=lst2.sort()
    if lst11==lst22:
        print("True")
    else:
        print("False")
else:
    print("False")
