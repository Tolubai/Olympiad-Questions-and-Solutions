# https://acmp.ru/index.asp?main=task&id_task=328

# n is maximum number of dots in domino
# if n = 3, domino dots are 00, 01, 02, 03, 11, 12, 13, 22, 23, 33
# types of digits --> n + 1 (00, 01, 02, 03)
# amount of every digits --> n + 2 (there are n + 2 (0, 1, 2, 3)

# arithmetic sum of 0 to n is (0 + n) * (n + 1) / 2
# total amount is  (0 + n) * (n + 1) * (n + 2) / 2

file_in = open('input.txt')
file_out = open('output.txt', 'w')

n = int(file_in.read())
total = (0 + n) * (n + 1) * (n + 2) // 2
file_out.write(str(total))

file_in.close()
file_out.close()