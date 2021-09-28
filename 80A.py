#https://codeforces.com/problemset/problem/80/A
inp = input()
inp = inp.split(" ")

num_1 = int(inp[0])
num_2 = int(inp[1])

#num_1,num_2 = 7,9
prime_numbers = [2,3]

def has_divisor(number_to_check,list_of_nums):
  for current_divisor in list_of_nums:
    if number_to_check % current_divisor == 0:
      return True
  return False

for current_num in range(2,num_2+1):
  if has_divisor(current_num,prime_numbers) == False:
    prime_numbers.append(current_num)

if prime_numbers[-1] != num_1:
  if prime_numbers[prime_numbers.index(num_1)+1] == num_2:
    print ("YES")
  else:
    print ("NO")
else:
  print ("NO")