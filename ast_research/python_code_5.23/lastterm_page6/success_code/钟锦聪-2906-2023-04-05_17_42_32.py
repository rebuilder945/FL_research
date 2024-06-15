def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    iShengyu = total_count
    for i in range(1,total_count//2):
        iShengyu = iShengyu - iShengyu//2 - 2
        if iShengyu ==0:
            print(i)
            break
main()


