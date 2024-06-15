def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=0
    s=0
    while i<total_count:
        i=(i+2)*2
        s=s+1
    print(s)
main()


