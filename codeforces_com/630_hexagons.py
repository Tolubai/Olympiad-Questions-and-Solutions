# https://codeforces.com/problemset/problem/630/D

# n = 0 --> 1
# n = 1 --> 1 + 6
# n = 2 --> 1 + 6 + 12

# total = 1 + 6 * (1 + n) * n // 2

number_of_cells = int(input())
total_amount_of_hexagons = (1 + 6 * (1 + number_of_cells) * number_of_cells // 2)
print(total_amount_of_hexagons)