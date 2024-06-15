def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    mai_count = total_count // 2 + 2
    i=1
    while mai_count < total_count:
            total_count-=mai_count
            mai_count = total_count // 2 + 2
            i+=1
    print(i)
main()


