def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    a = 1
    for x in range(n):
        if n/2-2 <= 0:
            break
        else:
            a += 1
            n = n-int(n/2)-2
    print(a)
main()


