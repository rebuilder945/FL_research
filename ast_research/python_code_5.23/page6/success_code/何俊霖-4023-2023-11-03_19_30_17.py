def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
        n=int(total_count)
        d=0
        while n >= 0:
            n=int(n/2)-2
            d+=1
        print(d)
main()


