# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=26&id_problem=152

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number = int(file_in.read())
file_out.write(f'The next number for the number {number} is {number + 1}.\n'
               f'The previous number for the number {number} is {number - 1}. ')
file_in.close()
file_out.close()