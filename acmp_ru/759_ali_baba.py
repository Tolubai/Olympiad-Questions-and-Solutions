# https://acmp.ru/index.asp?main=task&id_task=759

file_in = open('input.txt')
file_out = open('output.txt', 'w')

# # n – количество предметов в пещере
# # m – максимальное количество предметов, которые Али-Баба может унести с собой

# first way accepted from acmp.ru
num = list(map(int, file_in.read().split()))

n = num[0]
m = num[1]
price = num[2:]
price.sort()
total = 0
for i in range(m):
    if price[n - 1 - i] > 0:
        total += price[n - 1 - i]

file_out.write(str(total))


# second way

numbers = list(map(int, file_in.read().split()))
n = numbers[0]
numbers.remove(n)
m = numbers[0]
numbers.remove(m)

numbers.sort()
numbers.reverse()

max_numbers = numbers[:m]
total_price = 0

for i in range(m):
    total_price += max_numbers[i]

file_out.write(str(total_price))


file_in.close()
file_out.close()
