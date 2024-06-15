def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(i):
    j=0
    while True:
        if i<0 or i==0:
            break
        i=i/2-2
        j+=1
       
    print(j)
main()


