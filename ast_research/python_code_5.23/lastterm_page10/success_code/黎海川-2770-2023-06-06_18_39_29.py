def Method(s1,s2):
    # 字符串是不可变的无法排序，str转list
    list1=list(s1) 
    list2=list(s2)
    # 进行排序
    list1.sort()
    list2.sort()
    # list 转 str
    a = ''.join(list1)
    b = ''.join(list2)
    # 进行比较
    if a==b:
        return True
    else:
        return False


if __name__ == "__main__":
    A = input()
    B = input()
    zzz = Method(A, B)
    print(zzz)
