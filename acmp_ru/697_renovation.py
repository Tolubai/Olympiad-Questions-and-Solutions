# https://acmp.ru/index.asp?main=task&id_task=697

file_in = open('input.txt')
file_out = open('output.txt', 'w')

l, w, h = map(int, file_in.read().split())
amount_of_tins = ((l * h + w * h) * 2 + 15) // 16
file_out.write(str(amount_of_tins))

file_in.close()
file_out.close()