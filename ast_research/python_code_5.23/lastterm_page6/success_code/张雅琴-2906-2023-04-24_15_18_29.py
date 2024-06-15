def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    num=0
    while x>0:
        x=x-x//2-2
        num+=1
        print(num)
main()


