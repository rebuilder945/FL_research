def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(b):
    b=str(b)
    c=b
    s=0
    for i in range(int(b)):
        s+=int(c)
        c+=b
    print(s)

main()

