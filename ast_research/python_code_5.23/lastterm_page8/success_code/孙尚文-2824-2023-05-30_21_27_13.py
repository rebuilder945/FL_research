def strrindex(s,t):
    pos = 0
    pos1 = -1
    while True:
        pos = s.find(t,pos)
        if pos == -1:
            return -1
        else:
            pos1 = pos
        pos = pos + len(t)
        if s.find(t,pos)==-1:
                        return pos1
        else:
                        b=s.rfind(t)
                        return b
if __name__ == "__main__":
    s=input()
    t=input()
    print(strrindex(s,t))

