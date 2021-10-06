#https://codeforces.com/problemset/problem/165/A
num_points = int(input())

def convert_to_array(num_points):
  all_points = []
  for current_point in range(num_points):
    inp = input()
    inp = inp.split(" ")
    temp_array = []
    for current_num in inp:
      temp_array.append(int(current_num))
    all_points.append(temp_array)
  return all_points

def right_neighbor(current_point,all_points):
  for point in all_points:
    if current_point != point:
      if current_point[1] == point[1] and current_point[0] > point[0]:
        return True
  return False

def left_neighbor(current_point,all_points):
  for point in all_points:
    if current_point != point:
      if current_point[1] == point[1] and current_point[0] < point[0]:
        return True
  return False

def above_neighbor(current_point,all_points):
  for point in all_points:
    if current_point != point:
      if current_point[1] < point[1] and current_point[0] == point[0]:
        return True
  return False

def below_neighbor(current_point,all_points):
  for point in all_points:
    if current_point != point:
      if current_point[1] > point[1] and current_point[0] == point[0]:
        return True
  return False

collection = convert_to_array(num_points)
return_answer = 0

for current_point in collection:
  if right_neighbor(current_point,collection) == True and left_neighbor(current_point,collection) == True:
    if above_neighbor(current_point,collection) == True and below_neighbor(current_point,collection) == True:
      return_answer += 1

print (return_answer)

