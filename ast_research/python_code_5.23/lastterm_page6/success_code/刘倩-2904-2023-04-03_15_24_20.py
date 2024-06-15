def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for i in range(1,a):
        a+=a*(10**i)
print(a)
main()

