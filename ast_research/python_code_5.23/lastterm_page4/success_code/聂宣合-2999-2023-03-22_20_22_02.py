a=input()
a=a.split(" ")
str=input()
word=[int(x) for x in str.split()]
word1=int(word[0])
word2=int(word[1])
x=a[word1]
a[word1]=a[word2]
a[word2]=x
print(a)
