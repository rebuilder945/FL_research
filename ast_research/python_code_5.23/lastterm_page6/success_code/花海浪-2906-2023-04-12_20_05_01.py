def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=1
    for i in range(total_count):
        total_count=int(total_count-((total_count)/2+2))
        a+=1
        if total_count<=0:
            print(a)
            break
main()


