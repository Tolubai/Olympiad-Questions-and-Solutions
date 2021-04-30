# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=28&id_problem=161

file_in = open('input.txt')
file_out = open('output.txt', 'w')

height, up, down = map(int, file_in.read().split())
days = (1 + (height - down -1) // (up - down))  # okruglenie verh

file_out.write(str(max(1, days)))

file_in.close()
file_out.close()