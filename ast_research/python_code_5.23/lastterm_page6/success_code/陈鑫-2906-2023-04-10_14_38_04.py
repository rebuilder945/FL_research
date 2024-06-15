def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    while a>0:
        a=a/2-2
    print((a+2)*2)
main()


