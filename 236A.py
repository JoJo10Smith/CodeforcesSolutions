#https://codeforces.com/problemset/problem/236/A
char_name = input()
lst_letters = []
for current_character in char_name:
  lst_letters.append(current_character)

unique = list(set(lst_letters))
if len(unique) % 2 == 0:
  print ("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
