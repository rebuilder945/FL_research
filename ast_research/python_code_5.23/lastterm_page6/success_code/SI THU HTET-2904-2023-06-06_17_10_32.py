def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    t=str(a)
    for i in range(a):
          s+=int(t)
          t+=str(a)
    return print(s)
main()

