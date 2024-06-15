def main():
    s1=input()
    s2=input()
    print(solution(s1,s2))
def solution(s1,s2):
    a=list(s1)
    b=list(s2)
    a.sort()
    b.sort()
    if a==b:
        return True
    else:
        return False
main()
    




