def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    bb=0
    while True:
        if total_count<=0:
            break
        else:
            if total_count%2==0:
                total_count=total_count-total_count/2-2
                bb+=1
            else:
                total_count=total_count-(total_count-1)/2-2
                bb+=1
    print(bb)
main()


