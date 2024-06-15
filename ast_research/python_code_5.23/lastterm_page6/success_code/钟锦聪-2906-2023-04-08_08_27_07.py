def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    if total_count == 1 or total_count== 2 or total_count==3 or total_count==4:
        a=1
        print(a)
    elif total_count==5:
        b=2
        print(b)
    elif total_count >5:
        iShengyu = total_count
        for i in range(1,total_count//2):
            iShengyu = iShengyu - iShengyu//2 - 2
            if iShengyu !=0:
                continue
            print(i)
            break

main()


