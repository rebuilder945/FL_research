def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=0
    for i in range(100):
        n+=1
        total_count=total_count/2-2
        if total_count<=0:
            break
    print(n)
main()


