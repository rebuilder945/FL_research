strings = input().split()
n, m = map(int, input().split())

n_index = n - 1
m_index = m - 1

strings[n_index], strings[m_index] = strings[m_index], strings[n_index]

print(strings)

