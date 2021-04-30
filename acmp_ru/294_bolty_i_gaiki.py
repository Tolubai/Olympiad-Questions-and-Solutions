# https://acmp.ru/index.asp?main=task&id_task=294

file_in = open('input.txt')
file_out = open('output.txt', 'w')

bolt_before, bolt_lost_percent, bolt_price, nut_befor, nut_lost_percent, nut_price = map(int, file_in.read().split())

total_cost_befor = bolt_before * bolt_price + nut_befor * nut_price
bolt_after_lost = bolt_before // 100 * (100 - bolt_lost_percent)
nut_after_lost = nut_befor // 100 * (100 - nut_lost_percent)
pairsAfter = min(bolt_after_lost, nut_after_lost)
total_cost_after = pairsAfter * (bolt_price + nut_price)
total_cost_damage = total_cost_befor - total_cost_after
file_out.write(str(total_cost_damage))

file_in.close()
file_out.close()