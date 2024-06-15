def zhaodao(s):
    for i in s:
        if s.count(i)==1:
            return i
    return "None"
n=input()
print(zhaodao(n))
