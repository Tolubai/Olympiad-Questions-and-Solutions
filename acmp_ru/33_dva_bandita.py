# https://acmp.ru/index.asp?main=task&id_task=33

file_in = open('input.txt')
file_out = open('output.txt', 'w')

garry, larry = map(int, file_in.read().split())
garry_not_shoot = larry - 1
larry_not_shoot = garry - 1

file_out.write(f'{garry_not_shoot} {larry_not_shoot}')

file_in.close()
file_out.close()
