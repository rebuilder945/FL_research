def abc(s1,s2):
    s2_list=list(s2)  # str转换为list
    pos1=0
    stillok = True
    while pos1<len(s1) and stillok:  # 循环s1长度的次数
        pos2=0
        found = False
        while pos2<len(s2_list) and not found:  # 循环s2长度的次数
            if s1[pos1]==s2_list[pos2]:
                found=True
            else:
                pos2=pos2+1
        if found:
            s2_list[pos2] = None
        else:
            stillok=False
        pos1 = pos1+1
    return stillok
if __name__ == "__main__":
    zzz = abc("abcd","dcba")
    print(zzz)
s1=eval(input())
s2=eval(input())
print(abc(s1,s2))
