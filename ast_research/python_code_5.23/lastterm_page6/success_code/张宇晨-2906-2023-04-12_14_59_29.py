def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    while True:
        i=0
        total_count=total_count-((total_count/2)+2)
        i=i+1
        if total_count==0:
            break
    print(i)
main()


