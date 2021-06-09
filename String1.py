# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
from typing import NewType


def hello_name(name): 
  result =  'Hello ' + name + "!" 
  return result
    
hello_name('Bob')


################################################################################################################################################################


# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'


def make_abba(a, b):
  newWord = ''
  newWord = a+b+b+a
  print(newWord)
  return newWord

# make_abba('Hi', 'Bye')
# make_abba('Yo', 'Alice')
# make_abba('What', 'Up')

################################################################################################################################################################

# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
  newString = ''
  newString = "<" + tag + ">" + word + "</" + tag + ">"
  print(newString)
  return newString

# make_tags('i', 'Yay')
# make_tags('i', 'Hello')
# make_tags('cite', 'Yay')

################################################################################################################################################################


# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.


# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(str):
  result = ''
  newString = str[-2] + str[-1]
  result = newString * 3
  print(result)
  return result

# extra_end('Hello')
# extra_end('ab')
# extra_end('Hi')

################################################################################################################################################################


# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(out, word):
  frontOfOut = out[0] + out[1]
  backOfOut = out[2] + out[3]
  newString = frontOfOut + word + backOfOut
  return newString

# make_out_word('<<>>', 'Yay')
# make_out_word('<<>>', 'WooHoo')
# make_out_word('[[]]', 'word')

################################################################################################################################################################


# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".


# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'

def first_two(str):
  if(len(str) < 2):
    return str
  else:
    firstTwo = str[0] + str[1]
  print(firstTwo)
  return firstTwo

# first_two('Hello')
# first_two('abcdefg')
# first_two('ab')

################################################################################################################################################################


# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'

def first_half(str):
  newString = ''
  halfLength = int(len(str) / 2)
  for i in range(halfLength):
    newString += str[i]
  return newString


# first_half('WooHoo')
# first_half('HelloThere')
# first_half('abcdef')

################################################################################################################################################################

# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'

def without_end(str):
  newString = ''
  if(len(str) == 2):
    return newString
  for i in range(1, len(str) -1):
    newString += str[i]
  print(newString)
  return newString

# without_end('Hello')
# without_end('java')
# without_end('coding')

################################################################################################################################################################

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).


# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'


def combo_string(a, b):
  if(len(a) > len(b)):
    return b + a + b
  else:
    return a + b + a


################################################################################################################################################################

# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'

def chopFront(word):
  newWord = ''
  for i in range(1, len(word)):
    newWord += word[i]
  print(newWord)
  return newWord


def non_start(a, b):
  a = chopFront(a)
  b = chopFront(b)
  return a + b

# non_start('Hello', 'There')
# non_start('java', 'code')
# non_start('shotl', 'java')

################################################################################################################################################################

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(str):
  front2 = str[0] + str[1]
  newString = ''
  for i in range(2, len(str)):
    newString += str[i]
  newString += front2
  print(newString)
  return newString

# left2('Hello')
# left2('java')
# left2('Hi')


