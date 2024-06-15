def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
        a=0
        i=0
        if total_count<=3:
               print("1")
        else:
            for i in range(total_count):
                    if total_count>0:
                        total_count=(total_count+1)//2-2
                        a+=1
                        i+=1
            print(a)
main()


