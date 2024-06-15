def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum = 0
    current = a
     for i in range(a):
        if i == 0 and a == 10:  
            current = a
        else:
            current = current * 10 + a
        sum += current
    print(sum)
main()

