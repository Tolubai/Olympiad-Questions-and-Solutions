# https://acm.timus.ru/problem.aspx?space=1&num=1638

file_in = open('input.txt')
file_out = open('output.txt', 'w')

"""
t - thickness of book
c - thickness of cover
b - beginning page of book
e - ending page of book
"""

t, c, b, e = map(int, file_in.readline().split())

distance = abs(t + (b - e) * (2 * c + t))

file_out.write(str(distance))

file_in.close()
file_out.close()
