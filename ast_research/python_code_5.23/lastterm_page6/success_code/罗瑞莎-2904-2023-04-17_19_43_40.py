def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sums=[]
    while i<a:
        x=str(a)*(i+1)
        sums.append(x)
        i+=1
    print(sum(sums))
main()

