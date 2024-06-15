def judge(s1,s2):
    set1 = set(s1)
    set2 = set(s2)
    if set1 == set2:
        return True
    return False
s1 = input()
s2 = input()
judge(s1,s2)
