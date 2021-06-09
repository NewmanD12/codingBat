# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0


def count_evens(nums):
  evensCount = 0
  for i in range(len(nums)):
    if(nums[i] % 2 == 0):
      evensCount += 1
  return evensCount

##################################################################################################################################################################################################################

# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

def big_diff(list):
  max = list[0]
  min = list[0]
  diff = 0
  for i in range(len(list)):
    if(list[i] < min):
      min = list[i]
    if(list[i] > max):
      max = list[i]
  print(max)
  print(min)
  diff = max - min
  print(diff)
  return diff

# big_diff([10, 3, 5, 6])
# big_diff([7, 2, 10, 9])
# big_diff([2, 10, 7, 2])



##################################################################################################################################################################################################################

# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False


def has22(list):
  for i in range(len(list)-1):
    if(list[i] == 2 and list[i + 1] ==2):
      return True
  return False

##################################################################################################################################################################################################################


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(list):
    count = True
    total = 0

    for item in list:
        if(item == 6):
            count = False
        if(count):
            total += item
            continue
        if(item == 7):
            count = True
    return total

# sum67([1, 2, 2, 6, 99, 99, 7])

##################################################################################################################################################################################################################

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6



def sum13(list):
  sum = 0
  for i in range(len(list)):
    # print(list[i])
    if(list[i] == 13 or list[i - 1] == 13):
      list[i] == 0
      sum += list[i]
      continue
    else:
      sum += list[i]
  print(sum)    
  return sum

# sum13([1, 2, 2, 1])
# sum13([1, 1])
# sum13([1, 2, 2, 1, 13])
# sum13([1, 2, 13, 2, 1, 13])
# sum13([1, 2, 2, 1, 13]) 

##################################################################################################################################################################################################################

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(list):
  total = 0
  count = 0
  average = 0
  max = 0
  min = 0
  for i in range(len(list)):
    if(list[i] <= min):
      min = list[i]
      count += 1
      total += list[i]
    if(list[i] >= max):
      max = list[i]
      count += 1
      total += list[i]
    else:
      count += 1
      total += list[i]
  total -= max
  total -= min
  count -= 2
  average = total / count
  print(total)
  print(count)
  return average

centered_average([1, 2, 3, 4, 100])
    
