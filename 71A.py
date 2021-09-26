#https://codeforces.com/problemset/problem/71/A
num_words = int(input())
answers = []

for i in range(num_words):
  current_word = input()
  if len(current_word) > 10:
    print(current_word[0]+ str(len(current_word)-2)+current_word[-1])
  else:
    print(current_word)

for current_answer in answers:
  print (current_answer)
