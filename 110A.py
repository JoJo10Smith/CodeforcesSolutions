#https://codeforces.com/problemset/problem/110/A
number = input()
lucky_nums = 0

if len(number) > 0:
  for current_number in number:
    if current_number == "4" or current_number == "7":
      lucky_nums += 1

  if lucky_nums > 0:
    if lucky_nums % 4 == 0 or lucky_nums % 7 == 0:
      print ("YES")
    else:
      print ("NO")
  else:
    print ("NO")
else:
  print ("NO")
