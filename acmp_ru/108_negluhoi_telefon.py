# https://acmp.ru/index.asp?main=task&id_task=108

file_in = open('input.txt')
file_out = open('output.txt', 'w')

a = file_in.read()
file_out.write(a)

file_in.close()
file_out.close()