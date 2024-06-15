def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=0
    for i in range(0,100):
        total_count=total_count*0.5-2
        a=a+1
        while total_count==0:
            print(a)
main()


