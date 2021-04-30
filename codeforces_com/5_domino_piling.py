# https://codeforces.com/problemset/problem/50/A

rectangular_size = input('')
m, n = map(int, rectangular_size.split())

max_number_of_domino = (m * n) // 2

print(max_number_of_domino)