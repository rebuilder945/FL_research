def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    if total_count>0:
        if type(total_count/2)!=int:
            total_count=(total_count-1)/2-2
            count=count+1
        else:
            total_count=total_count/2-2
            count=count+1
    if total_count<=0:
        count=count
        break
    print(count)
main()


