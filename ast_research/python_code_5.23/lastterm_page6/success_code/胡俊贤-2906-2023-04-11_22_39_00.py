def main():
    total_count = int(input())
    calculate_days(total_count)
    print(calculate_days(total_count))
def calculate_days(total_count):
    day=0
    while not total_count == 0:
        if total_count%2==0:
            total_count=total_count/2-2
            day=day+1
        else :
            total_count=(total_count+1)/2-2
            day=day+1
    return day
main()


