#https://codeforces.com/problemset/problem/200/B
num_drinks = int(input())
inp = input()
inp = inp.split(" ")

lst = []
for x in range(len(inp)):
  lst.append(int(inp[x]))

total = 0
for i in range(len(lst)):
  total += lst[i]

print (total/num_drinks)
