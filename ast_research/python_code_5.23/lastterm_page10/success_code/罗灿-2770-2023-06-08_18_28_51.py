def dword(w1,w2):
    w1ls=[]
    w2ls=[]
    for i in w1:
        w1ls.append(i)
    w1ls.sort()
    for i in w2:
        w2ls.append(i)
    w2ls.sort()
    if w1ls==w2ls:
        return True
    
w1=input()
w2=input()
print(dword(w1,w2))
