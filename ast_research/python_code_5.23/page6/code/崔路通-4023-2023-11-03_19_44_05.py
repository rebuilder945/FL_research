def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    a=0
    b=total_count
    for i in range(b):
         if total_count-(total_count/2-2)>=0:
            a=a+1
        else:
            a=a+1
            break
print(a)

   
main()


