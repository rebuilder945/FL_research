from collections import Counter
s = input()
w = s.split()
c = Counter(w)
mc = max(c.values())
most_common = sorted(word for word,count in c.items() if count == mc)
for word in most_common:
    print(w,mc)
    
