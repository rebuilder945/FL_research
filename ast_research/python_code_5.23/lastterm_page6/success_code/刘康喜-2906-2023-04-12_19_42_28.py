def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    b=0
    while True:
        if a>0:

            b=b+1
            a=a-int(a)/2-2

        else:
            break
    print(b)

main()


