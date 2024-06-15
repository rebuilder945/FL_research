word = input().split()
n,m = input().split(" ")
n=int(n)
m=int(m)
word = list(word)
a = word[n]
word[n] = word [m]
word[m] = a
print(word)

