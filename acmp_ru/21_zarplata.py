# https://acmp.ru/index.asp?main=task&id_task=21

file_in = open('input.txt')
file_out = open('output.txt', 'w')

a, b, c = map(int, file_in.readline().split())
max_zarplata = max(a, b, c)
min_zarplata = min(a, b, c)
raznica = max_zarplata - min_zarplata
file_out.write(str(raznica))

file_in.close()
file_out.close()