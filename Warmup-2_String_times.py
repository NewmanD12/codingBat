
# Given a string and a non-negative int n, return a larger 
# string that is n copies of the original string.

def string_times(str, n):
    print(str * n)
    return str * n

# string_times('Hi', 2)

#######################################################################
# Given a string, return a new string made of every other char 
# starting with the first, so "Hello" yields "Hlo".


def string_bits(str):
    result = ""
    for x in range(0, len(str), 2):
        result += str[x]
    #   print(str[x])
    print(result)
    return result

# string_bits('Hello')


#######################################################################
# Given a string and a non-negative int n, we'll say that the front of 
# the string is the first 3 chars, or whatever is there if the string is 
# less than length 3. Return n copies of the front;

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
    while count < n:
        result = firstThreeLetters * n
        count += 1
    print(result)
    return result

# front_times('Chocolate', 2)
# front_times("Chocolate", 3)
# front_times('Abc', 3)


#######################################################################

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

#######################################################################
# Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    return count

# array_count9([1, 2, 9])
# array_count9([1, 9, 9])
# array_count9([1, 9, 9, 3, 9])


#######################################################################

# Given an array of ints, return True if one of the first 4 elements 
# in the array is a 9. The array length may be less than 4.

def array_front9(lst):
    lst = lst[:4]
    contains9 = False
    for i in lst:
        if i == 9:
            contains9 = True
    return contains9

# print(array_front9([1,2,9,3,4]))
# print(array_front9([1, 2, 3, 4, 9]))

#######################################################################
# Given an array of ints, return True if the sequence of numbers 1, 2, 
# 3 appears in the array somewhere.


def array123(nums):
    i = 0
    contains123 = False
    while i < len(nums) - 2:
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            contains123 = True
        i += 1
    # print(contains123)
    return contains123


array123([1, 1, 2, 3, 1])
array123([1, 1, 2, 4, 1])
array123([1, 1, 2, 1, 2, 3])
#######################################################################
# Given 2 strings, a and b, return the number of the positions where 
# they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" 
# yields 3, since the "xx", "aa", and "az" substrings appear in the same 
# place in both strings.


def string_match(a, b):
    substringListA = []
    substringListB = []
    count = 0
    for i in range(len(a) - 1):
        substringListA.append([a[i], a[i+1]])
    for i in range(len(b) - 1):
        substringListB.append([b[i], b[i+1]])

    for i in substringListA:
        if i in substringListB:
            substringListA.remove(i)
            count += 1
    print(count)
    return count

# string_match('xxcaazz', 'xxbaaz')
# string_match('abc', 'abc')
# string_match('aabbccdd', 'abbbxxd')


#######################################################################

# Given a string, return the count of the number of times that a substring 
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  listOfDoubles = []
  last2 = str[-2:]
  count = 0
  for i in range(len(str) - 2):
    listOfDoubles.append(str[i]+str[i+1])
  for i in listOfDoubles:
    if i == last2:
      count += 1
  return count

last2('hixxhi')
last2('xaxxaxaxx')
last2('axxxaaxx')

#######################################################################

# Given two strings, return True if either of the strings appears at the 
# very end of the other string, ignoring upper/lower case differences 
# (in other words, the computation should not be "case sensitive"). Note: s.lower() 
# returns the lowercase version of a string.

def end_other(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    res = False
    min_word = min(str_1, str_2)
    max_word = max(str_1, str_2)
    shortest = min(len(str_1), len(str_2))
    longest = max(len(str_1), len(str_2))
    print(shortest, longest, min_word, max_word)
    # if longest[-len(shortest):] == shortest:
    #     res = True
    # # print(res)
    # return res

# end_other('Hiabc', 'abc')
# end_other('abc', 'abXabc')
end_other('Z', '12xz') 
end_other('xyz', '12xyz')

