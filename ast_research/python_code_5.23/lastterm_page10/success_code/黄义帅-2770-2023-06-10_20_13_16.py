def is_anagram(s1, s2):  
    s1 = ''.join(sorted(s1))  
    s2 = ''.join(sorted(s2))  
    return s1 == s2  
  
if __name__ == '__main__':  
    s1, s2 = input().strip().split()  
    if is_anagram(s1, s2):  
        print('True')  
    else:  
        print('False')
