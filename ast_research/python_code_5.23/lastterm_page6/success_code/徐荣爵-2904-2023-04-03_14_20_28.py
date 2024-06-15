def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    N = 0
    for i in range(a):
        j = a - i
        N = N + j*a*10**i
    print(N)
main()

