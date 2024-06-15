def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b = [a]
        c = 0
        for i in range(1,a+1):
                e = b*i
                f = int("".join("%s"%id for id in e ))
                c+=f
        return c
main()

