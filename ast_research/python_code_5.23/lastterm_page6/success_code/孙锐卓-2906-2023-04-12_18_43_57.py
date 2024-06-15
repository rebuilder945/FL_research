def main():
    total_count = int(input())
    calculate_days(total_count)

def calculate_days(total_count):
    a=total_count
    c=0
    while True:
        if a%2==0:
            b=a*0.5+2
            a=a-b
            c+=1
        if a%2==1:
            b=(a-1)*0.5+2
            a=a-b
            c+=1
        if a<=0:
            break
    print(c)

main()


