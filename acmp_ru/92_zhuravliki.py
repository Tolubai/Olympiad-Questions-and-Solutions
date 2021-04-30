# https://acmp.ru/index.asp?main=task&id_task=92

file_in = open('input.txt')
file_out = open('output.txt', 'w')

total_amount_of_zhuravliki = int(file_in.read())

Petya = total_amount_of_zhuravliki // 6
Seryoja = Petya
Katya = Petya * 4

file_out.write(f'{Petya} {Katya} {Seryoja}')
file_in.close()
file_out.close()