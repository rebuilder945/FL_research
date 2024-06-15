def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
            s = 0
            for i in range(a):
                s += (a-i)*(a*(10**i))
            print(s)
main()

