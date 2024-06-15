def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total):
    d=0
    while total>0:
        total//=2
        total-=2
        d+=1
    print(d)
main()


