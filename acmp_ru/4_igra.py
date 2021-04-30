# https://acmp.ru/index.asp?main=task&id_task=4

file_in = open('input.txt')
file_out = open('output.txt', 'w')

first_digit = int(file_in.read())
last_digit = 9 - first_digit
file_out.write(f"{first_digit}9{last_digit}")

file_in.close()
file_out.close()