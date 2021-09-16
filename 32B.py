#https://codeforces.com/problemset/problem/32/B
borze = input()
decode = {
  ".":"0",
  "-.":"1",
  "--":"2"
  }


answer = ""
current_character = ""
for i in range(len(borze)):
  current_character += borze[i]
  if current_character in decode:
    answer += decode[current_character]
    current_character = ""

print (answer)

