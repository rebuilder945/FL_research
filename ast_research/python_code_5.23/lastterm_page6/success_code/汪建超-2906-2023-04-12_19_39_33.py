def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(N):
    icounter = 0
    while True:
        if N <= 0:
            break
        else:
            N = N/2 - 2
            icounter += 1
    print(icounter)
    
main()


