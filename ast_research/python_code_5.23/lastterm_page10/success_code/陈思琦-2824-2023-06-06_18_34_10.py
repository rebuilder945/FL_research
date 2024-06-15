def strrindex(s,t):
    pos = 0
    pos1 = -1
    while True:
        pos = s.find(t,pos)
        if pos == -1:
            return pos
        else:
            pos1 = pos
        pos = pos + len(t)
    a=s.find(t,pos)
    if a==-1:
        return pos1
    else:
        return a
if __name__ == "__main__":
    s=input()
    t=input()
    print(strrindex(s,t))

