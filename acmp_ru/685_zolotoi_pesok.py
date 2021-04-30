# https://acmp.ru/index.asp?main=task&id_task=685

file_in = open('input.txt')
file_out = open('output.txt', 'w')

a1, a2, a3, b1, b2, b3 = map(int, file_in.read().split())
a_max = max(a1, a2, a3)
a_min = min(a1, a2, a3)
a_mid = a1 + a2 + a3 - a_min - a_max

b_max = max(b1, b2, b3)
b_min = min(b1, b2, b3)
b_mid = b1 + b2 + b3 - b_min - b_max

total_price = a_max * b_max + a_mid * b_mid + a_min * b_min
file_out.write(str(total_price))

file_in.close()
file_out.close()