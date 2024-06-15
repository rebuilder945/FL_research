def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    iShengyu = total_count
    for i in range(0,total_count):
            iShengyu = iShengyu - iShengyu//2 - 2
            if iShengyu >0:
                continue
            print(i+1)
            break

main()


