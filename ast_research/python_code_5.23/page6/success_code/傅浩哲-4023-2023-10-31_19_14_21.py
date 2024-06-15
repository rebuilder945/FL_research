def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    while total_count>=0:
        a=int(total_count/2)+2
        total_count-=a
    print(total_count)
main()


