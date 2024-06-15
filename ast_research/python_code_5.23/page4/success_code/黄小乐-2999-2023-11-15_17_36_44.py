word = input().split(" ")
n,m = input().split(" ")
n=int(n)
m=int(m)
word = list(word)
word[n],word[m]=word[m],word[n]
print(word)
