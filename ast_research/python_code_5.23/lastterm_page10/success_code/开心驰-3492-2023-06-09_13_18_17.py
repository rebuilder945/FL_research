def main():
    s = input()
    ch = input()
    print(count(s,  ch))


def count(s, ch):
    b={}
    for i in range(len(s)):
        if s[i] not in b:
            b[s[i]]=1
        else:
            b[s[i]]+=1
    for i in b:
        if b[i]==1:
            return b[i]
    return None


main()


    
