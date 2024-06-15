def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=0
    while True:
        total_count=total_count-((total_count/2)+2)
        i=i+1
        if total_count<1:
            break
        if total_count==0:
            print(i)
        else:
            i=i+1
            print(i)
main()


