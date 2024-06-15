def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=0
    for x in range(10000):
        total_count=total_count-((total_count/2)+2)
        i=i+1
        if total_count==0:
            break
    print(i)
main()


