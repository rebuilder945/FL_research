m=input()
n=input()
while n in m:
    m=m.replace(n,"")
print(m)
