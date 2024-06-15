def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    b=total_count
    a=0
    while total_count-(total_count//2)>=3:
        a=a+1
        total_count=total_count-(total_count//2)
        if total_count<3:
            a=a+1
            break
print(a)
    
    
        
 

   
main()


