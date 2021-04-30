# https://acmp.ru/index.asp?main=task&id_task=312

file_in = open('input.txt')
file_out = open('output.txt', 'w')

a_1, a_2, n = map(int, file_in.read().split())

d = a_2 - a_1

a_n = a_1 + (n - 1) * d

file_out.write(str(a_n))

file_in.close()
file_out.close()