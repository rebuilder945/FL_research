def strrindex(s,t):
    pos = 0
    pos1 = -1
    while True:
        pos = s.find(t,pos)
        if pos == -1:
            icard[0:6]+"*"*8+icard[14:]
        else:
            pos1 = pos
        pos = pos + len(t)
    return pos1
if __name__ == "__main__":
    s=input()
    t=input()
    print(strrindex(s,t))

