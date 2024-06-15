def find_unique(lst):
    unique = eval(input())
    for i in lst:
        if lst.count(i) ==1:
            unique.append(i)
        if len(unique) > 0:
          return sorted(unique)
        else:
            return False
