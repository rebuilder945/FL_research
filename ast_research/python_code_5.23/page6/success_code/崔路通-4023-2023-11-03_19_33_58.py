def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=0
    for i in range(N):
        if total_count/2-2>=0:
            total_count=total_count/2-2
            a=a+1
        else:
             a=a+1
    print(a)
   
main()


