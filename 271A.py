#https://codeforces.com/problemset/problem/271/A
current_year = int(input())

def find_year(current_year):
  unique = False
  current_check = current_year +1
  lst_digits = []
  while unique == False:
    for current_num in str(current_check):
      lst_digits.append(int(current_num))
  
    if len(lst_digits) == len(set(lst_digits)):
      unique = True
      print (current_check)
    else:
      lst_digits = []
      current_check += 1


find_year(current_year)
    
  
