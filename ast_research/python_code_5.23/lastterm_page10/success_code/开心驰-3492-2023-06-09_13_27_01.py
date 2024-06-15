def main():
    s = input()
    print(count(s))


def count(s):
    b={}
    for i in range(len(s)):
        if s[i] not in b:
            b[s[i]]=1
        else:
            b[s[i]]+=1
    for i in b:
        if b[i]==1:
            return i
    return None


main()


    
