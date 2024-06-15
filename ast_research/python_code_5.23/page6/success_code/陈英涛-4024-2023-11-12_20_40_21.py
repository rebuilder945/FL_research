def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(b):
        d = []
        for i in range(1,b+1):
            c = int(str(b)*i)
            d.append(c)
        print(sum(d))
main()

