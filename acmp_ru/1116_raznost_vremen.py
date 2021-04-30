# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=28&id_problem=159

file_in = open('input.txt')
file_out = open('output.txt', 'w')

h1, m1, s1, h2, m2, s2 = map(int, file_in.read().split())
time_difference_in_second = (h2 - h1) * 60 * 60 + (m2 - m1) * 60 + (s2 -s1)

file_out.write(str(time_difference_in_second))

file_in.close()
file_out.close()
