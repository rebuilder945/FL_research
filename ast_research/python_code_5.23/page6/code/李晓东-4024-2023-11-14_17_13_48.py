def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    list = []
    for i in range(a):
        b = int(str(a)*(i+1))
        list.append(b)
    print(sum(list)）

main()

