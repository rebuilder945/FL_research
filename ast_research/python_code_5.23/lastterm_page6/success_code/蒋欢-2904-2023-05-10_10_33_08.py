def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        s=0
        for i in range(int(a)):
            b=int(a*(i+1))
            s+=b
            print(b)
        print(s)

main()

