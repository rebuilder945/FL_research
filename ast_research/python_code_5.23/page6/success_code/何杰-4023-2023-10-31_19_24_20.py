def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
     t=total_count
     i=0
     while True:
        t=t//2-2
        i+=1
        if t<0:
           break
     print(i)

main()


