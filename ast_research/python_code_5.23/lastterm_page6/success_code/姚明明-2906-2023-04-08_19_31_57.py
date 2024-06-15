def main():
    total_count = int(input())
    calculate_days(total_count)
    print("calculate_days(total_count)")
def calculate_days(total_count):
    i=0
    while total_count>4:
         total_count=total_count-int(total_count/2)-2
         i+=1
         if total_count<=4:
             break
    total_count=i
    return(total_count)

    
main()


