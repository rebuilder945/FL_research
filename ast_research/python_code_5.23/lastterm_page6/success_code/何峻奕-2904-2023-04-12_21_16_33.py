def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    if a<10:
        for i in range(a):
            a=a+10**i*a
        print(a)
main()

