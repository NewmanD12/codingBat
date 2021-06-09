# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# OR

def sleep_in2(weekday, vacation):
  return True if not weekday or vacation else False

# print(sleep_in2(False, False))
# print(sleep_in2(True, False))
# print(sleep_in2(False, True))

##################################################################################################################################################################################################################


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
  if(a_smile and b_smile):
    return True
  elif(not a_smile and not b_smile):
    return True
  else: 
    return False




# print(monkey_trouble(True, True))
# print(monkey_trouble(False, False))
# print(monkey_trouble(True, False))

##################################################################################################################################################################################################################


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
  if(a == b):
    sum = a + b
    return sum * 2
  else:
    return a + b

# print(sum_double(3, 2))
# print(sum_double(2, 2))

# OR

def sum_double2(a, b):
  return a + b if a != b else (a+b) * 2

# OR

sum_double3 = lambda a, b: (a + b) * 2 if a == b else (a + b)
# print(sum_double3(3, 2))
# print(sum_double3(2,2))


##################################################################################################################################################################################################################


# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(n):
  diff = 0
  if(n > 21):
    diff = n - 21
    return diff * 2
  else:
    diff = 21 - n
    return diff

# print(diff21(19))
# print(diff21(10))
# print(diff21(21))

# OR

def diff21two(n):
   pass



##################################################################################################################################################################################################################


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
  if(talking and (hour < 7 or hour > 20)):
    return True
  else: 
    return False
  

# print(parrot_trouble(True, 6))
# print(parrot_trouble(True, 7))
# print(parrot_trouble(False, 6))

##################################################################################################################################################################################################################

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  if((a + b == 10) or (a == 10 or b == 10)): 
    return True
  else:
    return False

# print(makes10(10, 10))
# print(makes10(9, 9))
# print(makes10(1, 9))

def makes10two(a, b):
  return True if (a + b == 10) or (a == 10 or b == 10) else False

# print(makes10two(10, 10))
# print(makes10two(9, 9))
# print(makes10two(1, 9))

makesTen = lambda a, b : True if (a + b == 10) or (a == 10 or b == 10) else False
 

##################################################################################################################################################################################################################

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(num):
  result = abs(100 - num)
  # print(result)
  if(abs(100 - num) <= 10 or abs(200 - num) <= 10):
    # print('True')
    return True
  else:
    # print('False')
    return False

near_hundred(93)

##################################################################################################################################################################################################################

# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

def pos_neg(a, b, negative):
  if(negative):
    if(a < 0 and b < 0):
      return True
    else:
      return False
  else:
    if(a < 0 and b > 0):
      return True
    if(a > 0 and b < 0):
      return True
    else:
      return False

##################################################################################################################################################################################################################

# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

def not_string(str):
  if(len(str) < 3):
    return 'not ' + str
  else:
    if(str[0] + str[1] + str[2] == 'not'):
      return str
    else:
      return 'not ' + str

##################################################################################################################################################################################################################
  
# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  result = ''
  for i in range(len(str)):
    if(i == n):
      continue
    else:
      result += str[i]
  return result

##################################################################################################################################################################################################################


# Given a string, return a new string where the first and last chars have been exchanged.


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  if(len(str) == 1):
    return str
  if(len(str) == 2):
    result = str[1] + str[0]
    print(result)
    return result
  if(len(str) > 2):
    front = str[0]
    back = str[-1]
    newString = ''
    result = ''
    for i in range(1, len(str)):
      newString += str[i]
      result = back + newString + front
    print(newString)
    print(result)

front_back('code')
front_back('a')
front_back('ab')
      
  
