# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=151
# Deleniya okurugleniem verh a /^ b = (a + b -1) / b

file_in = open('input.txt')
file_out = open('output.txt', 'w')

amount_of_gold_mm = int(file_in.read())
cost_for_work = (amount_of_gold_mm + 9) // 10
file_out.write(str(cost_for_work))

file_in.close()
file_out.close()