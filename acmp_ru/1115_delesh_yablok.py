# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=158

file_in = open('input.txt')
file_out = open('output.txt', 'w')

n, k = map(int, file_in.read().split())
each_one_has = k // n
remained = k % n
resentful_one = (n - remained) % n
file_out.write(f'{each_one_has} {remained} {resentful_one}')

file_in.close()
file_out.close()