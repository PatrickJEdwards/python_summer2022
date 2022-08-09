# You can find information on how to convert numbers to a different base here:
# https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm

# You can find information on how to convert numbers to roman numerals here:
# https://www.romannumerals.org/converter



# FINISHED!
def binarify(num): 
  """convert positive integer to base 2"""
  if num <= 0: 
      return '0'
  remain = []
  n_num = num
  while n_num != 0:
      remain.append(n_num % 2)
      n_num = n_num // 2
  remain.reverse()
  digits = map(str, remain)
  return ''.join(digits)


# FINISHED!
def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num <= 0:  return '0' 
  remain = []
  while num != 0:
      remain.append(num % base)
      num = num // base
  remain.reverse()
  digits = map(str, remain)
  return ''.join(digits)


# FINISHED!!!
def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string == "0" or base <= 0 : return 0 
  result = 0 
  # Split digits in int string.
  s_l_num = list(string)
  # Convert list to integer
  i_l_num = []
  for i in s_l_num:
      i_l_num.append(int(i))
  # Find length of string number.
  num_dig = list(range(0, len(string), 1))
  # Reverse length of num
  num_dig.reverse()
  # Do math.
  times = []
  for i in range(0, len(i_l_num)):
      times.append(i_l_num[i] * (base ** num_dig[i]))
  # Sum result:
  result = sum(times)
  return result


# FINISHED!!
def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  # Convert str1 to base 10.
  str1_num = []
  for i in list(str1):
      str1_num.append(int(i))
  str1_ndig = list(range(0, len(str1), 1))
  str1_ndig.reverse()
  times1 = []
  for i in range(0, len(str1_num)):
      times1.append(str1_num[i] * (base1 ** str1_ndig[i]))
  result1 = sum(times1)
  # Convert str2 to base 10.
  str2_num = []
  for i in list(str2):
      str2_num.append(int(i))
  str2_ndig = list(range(0, len(str2), 1))
  str2_ndig.reverse()
  times2 = []
  for i in range(0, len(str2_num)):
      times2.append(str2_num[i] * (base2 ** str2_ndig[i]))
  result2 = sum(times2)
  # Sum numbers
  result = result1 + result2
  return result

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  # Convert str1 to base 10.
  str1_num = []
  for i in list(str1):
      str1_num.append(int(i))
  str1_ndig = list(range(0, len(str1), 1))
  str1_ndig.reverse()
  times1 = []
  for i in range(0, len(str1_num)):
      times1.append(str1_num[i] * (base1 ** str1_ndig[i]))
  result1 = sum(times1)
  # Convert str2 to base 10.
  str2_num = []
  for i in list(str2):
      str2_num.append(int(i))
  str2_ndig = list(range(0, len(str2), 1))
  str2_ndig.reverse()
  times2 = []
  for i in range(0, len(str2_num)):
      times2.append(str2_num[i] * (base2 ** str2_ndig[i]))
  result2 = sum(times2)
  # Multiply results:
  result = result1 * result2
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result


# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.