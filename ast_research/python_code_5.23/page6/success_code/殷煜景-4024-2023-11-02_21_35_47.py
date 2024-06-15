def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=a
        c=a
        for i in range(1,b):
                    a=a+b*10**i
                    c=a+c
        print(c)
main()

