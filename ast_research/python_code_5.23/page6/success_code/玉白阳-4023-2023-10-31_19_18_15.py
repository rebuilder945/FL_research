def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    while x>0:
        x=x-(x//2+2)
        calculate_days+=1
    print(calculate_days)
main()


