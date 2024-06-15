def main():
    total_count = int(input())
    calculate_days(total_count)
y=0
def calculate_days(x):
    while x>1:
        x=x/2-2
        y+=1
    print(y)    

main()


