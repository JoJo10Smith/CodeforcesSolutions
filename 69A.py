#https://codeforces.com/problemset/problem/69/A
num_input = int(input())
position = [0,0,0]

for counter in range(num_input):
  current_force = input()
  current_force = current_force.split(" ")
  position[0] += int(current_force[0])
  position[1] += int(current_force[1])
  position[2] += int(current_force[2])

position.sort()
if position[0] == position[2] and position[1] == 0:
  print ("YES")
else:
  print ("NO")
