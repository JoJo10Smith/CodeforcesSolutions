#https://codeforces.com/problemset/problem/116/A
num_stops = int(input())
passengers = 0
capacity = 0

for current_stop in range(num_stops):
  inp = input()
  inp = inp.split(" ")
  delta = int(inp[1])-int(inp[0])

  passengers += delta
  if passengers > capacity:
    capacity = passengers

print (capacity)

  
