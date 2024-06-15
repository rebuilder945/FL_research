word dict = {}
while True:
word =input()if word == "q":break
if word in word dict:word dict[word] += 1 else:
word dict[word] = 1
max word
max count = o
for word, count in word dict.items():
if count > max count:
max word
= word max count = count
print(''，max word)
print(''，max count)


