# https://acmp.ru/index.asp?main=task&id_task=528

# k - level of castle
# n - number of angles
# n = 6 k = 1 --> total doors = 6
# n = 6 k = 2 --> total doors = 6 + 12 - 3 = 15
# n = 6 k = 3 --> total doors = 6 + 12 + 18 - 3 - 5 = 28

# k + 1 + (n-2) * (1 + ..+ k)
# k + 1 + (n -2) * (1+k) * k /2

file_in = open('input.txt')
file_out = open('output.txt', 'w')

n, k = map(int, file_in.readline().split())
total_doors = (k + 1) + (n-2) * (k+1) * k // 2
file_out.write(str(total_doors))

file_in.close()
file_out.close()