# https://acmp.ru/index.asp?main=task&id_task=554

# n = 0 --> 1
#               +1
# n = 1 --> 2
#               +2
# n = 2 --> 4
#               +3
# n = 3 --> 7

# sum of arithmetic numbers
# 1 + 1 + 2 + 3 +..

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number_of_cutting = int(file_in.readline())

number_of_pieces = (1 + number_of_cutting) * number_of_cutting // 2 + 1

file_out.write(str(number_of_pieces))

file_in.close()
file_out.close()