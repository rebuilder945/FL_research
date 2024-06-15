def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
        a=total_count        
        b=0
        while a >0:      
                a=a/2-2
                b +=1
        print(b)
                
main()


