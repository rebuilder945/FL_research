def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[]
    for i in range(a):
        c=str(a)*i
        b.append(int(c))
    return sum(b)
main()

