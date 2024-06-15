def main():
    total_count = int(input())
    calculate_days(total_count)
    print(calculate_days(total_count)
def calculate_days(total_count):
    x=1
    if total_count>4:
        total_count=total_count-int(total_count/2)-2
        x+=1
    esle:
        return x

    
main()


