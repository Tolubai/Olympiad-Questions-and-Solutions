# https://acmp.ru/index.asp?main=task&id_task=263

file_in = open('input.txt')
file_out = open('output.txt', 'w')

number_of_stations, home_station, work_station = map(int, file_in.read().split())
max_num = max(home_station, work_station)
min_num = min(home_station, work_station)
number_of_min_stations = min((max_num - min_num - 1), (number_of_stations + min_num - max_num - 1))

file_out.write(str(number_of_min_stations))

file_in.close()
file_out.close()
