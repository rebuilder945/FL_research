def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    count=0
    day=0
    while count<total_count:
        day+=1
        if day==1:
            count+=total_count//2+2
        else:
            count+=(count//2)+2
    print(day)
main()


