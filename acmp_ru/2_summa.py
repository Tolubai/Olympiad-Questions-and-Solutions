# https://acmp.ru/index.asp?main=task&id_task=2

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number = int(file_in.read())
number_interval = abs(number - 1) + 1
arithmetic_sum_of_number = ((1 + number) * number_interval) // 2
file_out.write(str(arithmetic_sum_of_number))

file_in.close()
file_out.close()