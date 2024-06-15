from collections import Counter
s = input()
w = s.split()
c = Counter(w)
mc = max(c.values())
mw = sorted(word for word,count in c.items() if c == mc)
for word in mw:
    print(w,mc)
