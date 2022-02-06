# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

from decimal import Rounded
import re


def lucky_sum(a, b, c):
  if((c == 13) and b != 13 and a != 13):
    return a + b
  if(b == 13 and a != 13):
    return a
  if(a == 13):
    return 0
  else:
    return a + b + c



##################################################################################################################################################################################################################

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def fix_teen(n):
  n = 0
  return n



def no_teen_sum(a, b, c):
  if((a < 20) and (a > 12) and (a != 15) and (a != 16)):
    a = fix_teen(a)
  if((b < 20) and (b > 12) and (b != 15) and (b != 16)):
    b = fix_teen(b)
  if((c < 20) and (c > 12) and (c != 15) and (c != 16)):
    c = fix_teen(c)
  return a + b + c

# no_teen_sum(1, 2, 3)
# no_teen_sum(2, 13, 1)
# no_teen_sum(2, 1, 14)

  
##################################################################################################################################################################################################################
  
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().


# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round10(n):
  rounded = round(n/10)*10
  # print(rounded)
  return int(rounded)

def round_sum(num_1, num_2, num_3):
  num_1 = round10(num_1)
  num_2 = round10(num_2)
  num_3 = round10(num_3)
  # print(num_1 + num_2 + num_3)
  return num_1 + num_2 + num_3

round_sum(10, 10, 19)

######################################################

# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the 
# absolute value of a number.

# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
  res = False
  if (abs(a-b) < 2 and abs(a-c) > 1 and abs(b-c) > 1) or (abs(a-c) < 2 and abs(a-b) > 1 and abs(c-b) > 1):
    res = True
  print(res)
  return res

close_far(1, 2, 3)

    



