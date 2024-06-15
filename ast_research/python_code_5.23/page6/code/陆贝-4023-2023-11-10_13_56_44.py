def main():
    total_count = int(input())
    calculate_days(total_count)
ef calculate_days(total_count):
    t=total_count
    day=0
    while t>0:
        t=0.5*t-2
        day=day+1
    print(day)
main()


