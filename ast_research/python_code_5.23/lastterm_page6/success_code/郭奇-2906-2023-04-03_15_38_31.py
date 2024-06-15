def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
        a=total_count        
        if a >0:      
                a=a/2-2
        else: 
                print(total_count//a)
main()


