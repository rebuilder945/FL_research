def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        res = 0
        tail = 0
        for i in range(a,0,-1):
            res += a*(10**tail)*i
            tail += 1
        print(res)
main()

