# https://acmp.ru/index.asp?main=task&id_task=2

# Arithmetic progression  is a sequence of numbers such that the difference between
# the consecutive terms is constant.
# For instance, the sequence 5, 7, 9, 11, 13, 15, . . . is an arithmetic progression
# with a common difference of 2.

#   a_1, a_2, a_3,....a_n  where a_2 - a_1 = a_3 - a_2 = ....= d (difference)

# n_th term of arithmetic sequence is a_n = a_m + (n-m) * d
# sum of arithmetic sequence s = (a_1 + a_n) * n / 2

# number interval form m to n is |n - m|
# amount of numbers in number interval is |n-m| + 1

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number = int(file_in.read())
number_interval = abs(number - 1) + 1
arithmetic_sum_of_number = ((1 + number) * number_interval) // 2
file_out.write(str(arithmetic_sum_of_number))

file_in.close()
file_out.close()
