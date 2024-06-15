def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
    N = total_count
    for i in range(total_count):
        x = int(N * 0.5)
        N -= x+2
        t = i+1
        if N <= 0:
            break
        else:
            pass
    print(t)
main()


