def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    days=0
    while x>0:
        x=x/2-2
        days+=1
    print(days)
main()


