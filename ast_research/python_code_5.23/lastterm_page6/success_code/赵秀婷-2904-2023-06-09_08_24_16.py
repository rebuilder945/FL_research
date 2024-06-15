def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    i=1
    s=0
    while i <= a:
        s=s+int(str(a)*i)
        i=i+1
    return s
l=calculate_sum(n)
print(l)
main()

