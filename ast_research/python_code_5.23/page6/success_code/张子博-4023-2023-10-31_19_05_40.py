def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    p=total_count
    if p%2==1:
        p+=1
        for i in range(p):
            p=p-p/2-2
            if p<=0:
                print(i+1)
                break
    else:
        for i in range(p):
            p=p-p/2-2
            if p<=0:
                print(i+1)
                break
main()


