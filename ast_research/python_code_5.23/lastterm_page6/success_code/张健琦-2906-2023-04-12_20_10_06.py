def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=0
    for i in range(9999):
        if total_count/2-2>4:
            total_count=total_count/2-2
            a+=1
        else:
             a+=2
             break
    print(a)
main()


