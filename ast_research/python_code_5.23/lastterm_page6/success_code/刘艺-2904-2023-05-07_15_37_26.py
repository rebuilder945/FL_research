def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    i = 0
    list = []
    while i < a:
        x =str(a)*(i+1)
        list.append(int(x))
        i += 1
    print(sum(list))
main()

