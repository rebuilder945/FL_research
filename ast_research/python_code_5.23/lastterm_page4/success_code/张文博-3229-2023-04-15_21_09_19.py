
from collections import Counter  
zs = int(input())  
for i in range(zs):  
    a = int(input())  # 这个牌组的个数  
    b = input().split()  # 具体剩下的牌  
    c = Counter(b).most_common(a)  # 次数排在前n的数c d e  
    d = list(c[-1])[0]  
    print("Case #%d:"%(i+1),d)  

