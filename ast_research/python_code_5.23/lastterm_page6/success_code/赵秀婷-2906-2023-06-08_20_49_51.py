def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=1
    while (total_count%2-2)>0:
        i=i+1
    print(i)
main()


