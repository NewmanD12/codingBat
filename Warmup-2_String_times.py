
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  print(str * n)
  return str * n
  
# string_times('Hi', 2)

########################################################################################################################################################################################

# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  result = ""
  for x in range(0, len(str), 2):
    result += str[x]
  #   print(str[x])
  print(result)
  return result

# string_bits('Hello')


########################################################################################################################################################################################

# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
  count = 0
  firstThreeLetters = ""
  result = ""
  i = 0
  while(i <= 2):
    firstThreeLetters += str[i]
    i += 1
  # print(firstThreeLetters)
  while(count < n):
    result = firstThreeLetters * n
    count += 1
  print(result)
  return result

# front_times('Chocolate', 2)
# front_times("Chocolate", 3)
# front_times('Abc', 3)


########################################################################################################################################################################################


# Given a non-empty string like "Code" return a string like "CCoCodCode".


# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'


def string_splosion(str):
  explodedString = ""
  result = ""
  for i in range(len(str)):
    result += str[i]
    explodedString += result
  print(explodedString)


# string_splosion("Code")
# string_splosion("abc")
# string_splosion("ab")

########################################################################################################################################################################################

# Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if(nums[i] == 9):
      count += 1
  return count

# array_count9([1, 2, 9])
# array_count9([1, 9, 9])
# array_count9([1, 9, 9, 3, 9])


########################################################################################################################################################################################


# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(nums):
  for i in range(4):
    if(nums[i] == 9):
      print("True")
      return True
  print("False")
  return False
  

# array_front9([1, 2, 9, 3, 4])
# array_front9([1, 2, 3, 4, 9])
# array_front9([1, 2, 3, 4, 5])

########################################################################################################################################################################################


