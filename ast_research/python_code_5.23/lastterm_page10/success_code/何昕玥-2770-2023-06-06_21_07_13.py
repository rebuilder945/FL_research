def main():
    s1=input()
    s2=input()
    print(solution(s1,s2))
def solution(s1,s2):
    if len(s1)==len(s2):
        for i in s1:
            if s1.count(i)!=s2.count(i):
                return False
        return True
    else:
        return False
main()
