def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
    a = total_count/2 + 2
    b = total_count - a
    n = 1
    while b > 0:
        a = total_count/2 + 2
        b = total_count - a
        n += 1
    print(n)
main()


