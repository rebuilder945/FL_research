word = input().split()
n,m = input().split(" ")
n=int(n)
m=int(m)
word = list(word)
ls = word[n]
del word[n]
word.insert(m,ls)
print(word)

