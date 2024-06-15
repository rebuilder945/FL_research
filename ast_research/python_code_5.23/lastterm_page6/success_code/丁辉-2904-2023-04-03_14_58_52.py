def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(b):
    b=str(b)
    c=b
    s=0
    for i in range(int(b)):
        c+=b
        s+=int(c)
    print(s)

main()

