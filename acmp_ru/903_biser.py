# https://acmp.ru/index.asp?main=task&id_task=903

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number_of_busins_color = int(file_in.read())
file_out.write(str(number_of_busins_color + 1))


file_in.close()
file_out.close()