def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=0
    while total_count!=0:
        if total_count%2==0:
            i+=1
            total_count=total_count/2-2
        elif total_count%2!=0:
            i=i+1
            total_count=total_count-(total_count-1)/2-2
    print(i)
main()


