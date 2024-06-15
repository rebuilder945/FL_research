def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a = 0
    if total_count % 2 == 0 :
        total_count = total_count-total_count / 2 - 2
        a += 1
    if total_count == 1 or total_count == 2:
        a += 1
    print(a)
main()


