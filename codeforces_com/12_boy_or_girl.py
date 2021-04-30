# https://codeforces.com/problemset/problem/236/A

user_name = input('')
distinct_characters = ''.join(set(user_name))

answer = ''

if len(distinct_characters) % 2 == 0:
    answer = 'CHAT WITH HER!'
else:
    answer = 'IGNORE HIM!'

print(answer)