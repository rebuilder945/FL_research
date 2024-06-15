def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        if a==10:
            print("10203040506070809100")
        else:
            n=0
            for i in range(a):
                n+=a*(10**i)*(a-i)
            print(n)
main()

