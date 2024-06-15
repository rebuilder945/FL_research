def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    N = 0
    for i in range(a):
        j = i + 1
        N = N + j*a*10**i
    N = str(N)[::-1]
    N = int(N)
    print(N)
main()

