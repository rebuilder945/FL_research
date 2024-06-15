n=eval(input())
fenmu=2
fenzi=1
he=0
for i in range(n):
    shuzi=fenmu/fenzi
    he+=shuzi
    yuanfenzi=fenzi
    fenzi=fenmu
    fenmu+=yuanfenzi
print("%.4f"%he)
