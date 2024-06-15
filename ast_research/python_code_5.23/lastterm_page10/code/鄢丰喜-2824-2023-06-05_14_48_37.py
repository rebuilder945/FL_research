def strrindex(s,t):
    pos = 0
    pos1 = -1
    while True:
        pos = s.find(t,pos)
        if pos == -1:
            pos  =  pos1
        else:
            pos1 = pos
        pos = pos + len(t)
           return pos
if __name__ == "__main__":
    s=input()
    t=input()
    print(strrindex(s,t))

