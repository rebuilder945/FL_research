words = []
Words = []
for i in range(ord('a'),ord('z')+1):
    words += chr(i)
for i in range(ord('A'),ord('Z')+1):
    Words += chr(i)    
wword = dict(list(zip(words,words[::-1]))+list(zip(Words,Words[::-1])))
s = input()
t = s
s1 = ''
n = len(t)
for i in (t):
    if i in wword.keys():
        s1 += wword[i]
    else:
        s1 += i
print(s)
print(s1)

