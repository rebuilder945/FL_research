def main():
    s1 = input()
    s2 = input()
    print(solution(s1,s2))
def solution(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    if alist1 == alist2:
        return True
    else:
        return False
    main()
