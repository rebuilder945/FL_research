def main():
    s1=input()
    s2=input()
    print(And(s1,s2))

def And(s1,s2):
    A1=list(s1)
    A2=list(s2)
    As1=A1.sort()
    As2=A2.sort()
    if As1==As2:
        return True
    else:
        return False
main()

    

