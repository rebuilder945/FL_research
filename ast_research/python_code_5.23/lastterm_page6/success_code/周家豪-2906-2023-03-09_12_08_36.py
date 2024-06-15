def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    day=0
    while total_count > 0:
        sold=(total_count//2)+2
        total_count=total_count-sold
        day+=1
    print(day)
main()


