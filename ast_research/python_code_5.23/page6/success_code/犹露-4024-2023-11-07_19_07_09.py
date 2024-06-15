def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b =[]
    for i in range(a):
        m = int(str(a)*(i+1))
        b.append(m)
        c = sum(b)
    print(c)

main()

