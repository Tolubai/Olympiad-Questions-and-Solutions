# https://acmp.ru/index.asp?main=task&id_task=3

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number = int(file_in.read())
number_square = number ** 2
file_out.write(str(number_square))

file_in.close()
file_out.close()