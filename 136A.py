#https://codeforces.com/problemset/problem/136/A
num_friends = int(input())
give_gifts = input()
give_gifts = give_gifts.split(" ")
answer = ""

for current_receiver in range(1,num_friends+1):
  answer += str(give_gifts.index(str(current_receiver))+1)
  answer += " "

print (answer)
