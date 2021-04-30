# https://acmp.ru/index.asp?main=task&id_task=86

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number_of_cells_in_chess = int(file_in.read())

max_amount_of_queens = number_of_cells_in_chess ** 2 - (number_of_cells_in_chess - 1) * 3 - 1

file_out.write(str(max_amount_of_queens))

file_in.close()
file_out.close()