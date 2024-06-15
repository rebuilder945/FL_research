def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    M = a
    Num = M
    n = 0
    S = a // 10
    if S > 0:
        for i in range(a-1):
            n = n+1
            M = M + a*(10**(i+S+n))
            Num = Num + M
    else:
        for i in range(a-1):
            M = M + a*(10**(i+1))
            Num = Num + M
main()

