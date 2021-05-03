# https://acmp.ru/index.asp?main=task&id_task=1

# sum = a + b

file_in = open('input.txt')
file_out = open('output.txt', 'w')

a, b = map(int, file_in.readline().split())
file_out.write(str(a + b))

file_in.close()
file_out.close()
