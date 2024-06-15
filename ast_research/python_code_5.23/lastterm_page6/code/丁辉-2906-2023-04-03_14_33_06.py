def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
i=0
a=0
while i<total_count:
    i=(2+i)*2
    a+=1
print(a)
main()


