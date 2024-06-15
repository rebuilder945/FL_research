def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    left=int((total_count/2)-2)
    for x in range(total_count):
        ghjk=int((left/2)-2)
        if ghjk==0:
            print(x+2)
            break
main()


