# https://acm.timus.ru/problem.aspx?space=1&num=1327&locale=ru

file_in = open('input.txt')
file_out = open('output.txt', 'w')

day_started, day_finished = map(int, file_in.readline().split())
amount_of_predohraniteli = (day_finished + 1) // 2 - day_started // 2

file_out.write(str(amount_of_predohraniteli))

file_in.close()
file_out.close()
