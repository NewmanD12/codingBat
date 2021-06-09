# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

list1 = [1, 2, 6]
list2 = [6, 1, 2, 3]
list3 = [13, 6, 1, 2, 3]

def first_last6(list):
  # print(list[0], list[-1])

  if(list[0] == 6 or list[-1] == 6):
    print("true")
    return True
  else:
    print("false")
    return False
  

# first_last6(list1)
# first_last6(list2)
# first_last6(list3)

# OR

def first_last6Two(list):
  return True if (list[0] == 6) or (list[-1] == 6) else False

# OR

last6 = lambda list : True if (list[0] == 6) or (list[-1] == 6) else False

##################################################################################################################################################################################################################
 
# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True

def same_first_last(nums):
  if(len(nums) > 0 and (nums[0] == nums[-1])):
    return True
  else: 
    return False

# same_first_last([1, 2, 3])
# same_first_last([1, 2, 3, 1])
# same_first_last([1, 2, 1])

##################################################################################################################################################################################################################

# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


# make_pi() → [3, 1, 4]
def make_pi():
  array = [3, 1, 4]
  return array

##################################################################################################################################################################################################################
  
# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True

def common_end(list1, list2):
  if(list1[-1] == list2[-1] or (list1[0] == list2[0]) ):
    return True
  else: 
    return False

##################################################################################################################################################################################################################

# Given an int array length 2, return True if it contains a 2 or a 3.


# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(list):
  firstNum = list[0]
  secondNum = list[1]
  if(firstNum == 2 or firstNum == 3):
    return True
  elif(secondNum == 2 or secondNum == 3):
    return True
  else:
    return False

##################################################################################################################################################################################################################

# Given an array of ints length 3, return the sum of all the elements.


# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

def sum3(list):
  sum = 0
  for i in range(len(list)):
    sum += list[i]
  return sum
    


##################################################################################################################################################################################################################

# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.


# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]

def make_ends(nums):
  newList = []
  newList.append(nums[0])
  newList.append(nums[-1])
  return newList

##################################################################################################################################################################################################################

# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]

def rotate_left3(nums):
  nums = [nums[1], nums[2], nums[0]]
  return nums

##################################################################################################################################################################################################################

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.


# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

def middle_way(a, b):
  newList = []
  newList.append(a[1])
  newList.append(b[1])
  return newList

##################################################################################################################################################################################################################


# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


# reverse3([1, 2, 3]) → [3, 2, 1]
# reverse3([5, 11, 9]) → [9, 11, 5]
# reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
  nums = [nums[2], nums[1], nums[0]]
  return nums

##################################################################################################################################################################################################################
  
# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(list):
  biggestNum = 0
  if(list[0] > list[-1]):
    biggestNum = list[0]
  else:
    biggestNum = list[-1]
  list = [biggestNum, biggestNum, biggestNum]
  return list



max_end3([1, 2, 3])
max_end3([11, 5, 9])
max_end3([2, 11, 3])

##################################################################################################################################################################################################################

# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2

def sum2(nums):
  sum = 0
  if(len(nums) == 0):
    return sum
  if(len(nums) ==1):
    sum = nums[0]
    return sum
  else:
    sum = nums[0] + nums[1]
    return sum

