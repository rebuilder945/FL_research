def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=0
    while not total_count <=0:
        b=int(total_count/2)
        total_count -=b+2
        a+=1
    print(a)
main()


