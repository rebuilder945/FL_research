def main():
    total_count = int(input())
    calculate_days(total_count)
def    calculate_days(total_count):
                i=1
                total_count=total_count-total_count //2-2
                if total_count>0:
                        i+=1
                print(i)
main()


