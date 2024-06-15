def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(gua):
    days=0
    while gua>0:
        gua=gua/2-2
        days+=1
    print(days)
main()


