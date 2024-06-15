def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=0
    while(total_count>0):
        m=total_count//2
        total_count=total_count-m-2
        a+=1
    print(a)
main()


