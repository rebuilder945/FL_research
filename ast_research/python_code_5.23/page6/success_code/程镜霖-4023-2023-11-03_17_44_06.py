def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    x=[]
    for i in range(total_count):
        if total_count!=0:
           total_count=total_count/2-2
        else:
            x.append(i)
    return x
main()


