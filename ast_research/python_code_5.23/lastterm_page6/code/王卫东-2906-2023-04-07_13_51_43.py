def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
        y=0
       while  total_count >0:
            total_count = total_count-(total_count//2+2)
             y=y+1
       print(y)
main()


