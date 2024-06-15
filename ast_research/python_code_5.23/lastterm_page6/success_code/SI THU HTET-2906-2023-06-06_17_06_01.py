def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    Days=1
    for i in range(1,total_count+1):
        if total_count>4:
            Days+=1
            total_count=total_count-total_count//2-2
        else:
            return print(Days)
        
main()


