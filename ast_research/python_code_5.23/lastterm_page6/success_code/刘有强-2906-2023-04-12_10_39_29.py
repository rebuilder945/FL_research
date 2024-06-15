def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    nss=0
    while total_count > 0:
        total_count = int(total_count/2)-2
        nss+=1
    print(nss)
main()


