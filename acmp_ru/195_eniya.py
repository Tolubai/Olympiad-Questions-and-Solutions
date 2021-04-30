# https://acmp.ru/index.asp?main=task&id_task=195

file_in = open('input.txt')
file_out = open('output.txt', 'w')

n, a, b = map(int, file_in.read().split())

amount_of_thorium_sulfide = n * (a * b) * 2

file_out.write(str(amount_of_thorium_sulfide))

file_in.close()
file_out.close()