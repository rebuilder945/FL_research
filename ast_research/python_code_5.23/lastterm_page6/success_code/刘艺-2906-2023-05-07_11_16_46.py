def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    i = 0
    while a > 0:
        a -= int(a/2) + 2
        i += 1
    print(i)
main()


