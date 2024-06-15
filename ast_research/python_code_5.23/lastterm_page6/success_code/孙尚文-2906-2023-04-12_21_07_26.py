def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    c=0
    while total_count>0:
        a=total_count/2
        if a%1==0:
            total_count=total_count-a-2
            c+=1
        else:
            b=a-0.5
            total_count=total_count-b-2
            c+=1
    print(c)
main()


