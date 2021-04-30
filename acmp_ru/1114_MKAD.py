# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=157

file_in = open('input.txt')
file_out = open('output.txt', 'w')

v, t = map(int, file_in.read().split())
point = ((v * t) % 109 + 109) % 109 + 1
file_out.write(str(point))

file_in.close()
file_out.close()