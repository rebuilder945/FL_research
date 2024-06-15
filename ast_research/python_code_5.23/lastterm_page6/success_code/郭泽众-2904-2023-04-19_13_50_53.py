def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(num):
    sList = []
    for i in range(1,num+1):
        sList.append(int(str(num) * i))
    print(sum(sList))
main()

