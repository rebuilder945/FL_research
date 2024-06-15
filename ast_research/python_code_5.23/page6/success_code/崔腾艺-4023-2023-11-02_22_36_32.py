def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=0
    while total_count>0:
        if total_count%2==0:
            i+=1
            total_count=total_count/2-2
        else:
            i=i+1
            total_count=total_count/2-1.5
    print(i)
main()


