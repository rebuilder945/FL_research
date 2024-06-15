def main():
    s1=input()
    s2=input()
    print(solution(s1,s2))
def solution(s1,s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False
main()
