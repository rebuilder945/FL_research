def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i = 0
    s = total_count
    while s>0:
        i = i + 1
        s = s - int(s/2)
        if s>2:
            s = s - 2
        else:
            break
    print(i)
main()


