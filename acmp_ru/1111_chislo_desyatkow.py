# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=154

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number = int(file_in.read())
file_out.write(str(number // 10 % 10))

file_in.close()
file_out.close()