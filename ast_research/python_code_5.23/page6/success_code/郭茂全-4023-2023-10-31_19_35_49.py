def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=0
    while total_count>0:
        total_count=int(total_count/2)-2
        n+=1
    print(n)
main()


