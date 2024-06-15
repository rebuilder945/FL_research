def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=0
    for i in range(total_count):
        a+=1
        total_count=total_count-((total_count)/2+2)
        if total_count<=0:
            break
    print(a)
main()


