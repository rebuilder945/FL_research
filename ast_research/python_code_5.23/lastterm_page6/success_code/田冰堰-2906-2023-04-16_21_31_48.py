def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    M=1
    if total_count/2+2>4:
        M+=1
    print(M)
main()


