def main():
    total_count = int(input())
    calculate_days(total_count)
        n = 0
        def calculate_days(total_count):
            while total_count > 0:
                total_count = 0.5*total_count-2
                n += 1
            print(n)
main()


