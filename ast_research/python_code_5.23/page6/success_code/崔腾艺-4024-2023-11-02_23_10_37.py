def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        n=0
        for i in range(a):
            n+=a*(10**i)*(3-i)
        print(n)
main()

