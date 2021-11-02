#https://codeforces.com/problemset/problem/266/A
num_rocks = int(input())
rock_order = input()
same_rocks = 0

for current_index in range(num_rocks-1):
  if rock_order[current_index] == rock_order[current_index + 1]:
    same_rocks += 1

print (same_rocks)
