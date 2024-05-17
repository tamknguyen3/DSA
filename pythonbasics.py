# a // b divides a by b and returns the integer part
# string concatenation
# str() converts non-string into a string
# len() return length of a string 
# .upper() and .lower() built-in methods
# indexing string[number] returns one char 
# slicing string[:4] returns a chunk of chars
# .replace(string, string) method replaces substrings within a string with another substring
# .strip() method removes (by default) the whitespace at the beginning or end of a string

# check if substring is in a string -- in keyword -- stored as a boolean value 
string = "I am a Python programmer!"
substring = "Python"
Python_in_string = substring in string # -- not in -- basically does the opposite 
print(Python_in_string)

# int() and float() functions converts value into their data types respectively
# scientific numbers e or E meaning -- times 10 to the power
# complex numbers -- real and imagine part -- in python using j instead of i 
# incrementing += and decrementing -=      applies to other operators too: **=, //=
# Boolean comparisons == != > < >- <=
# Boolean operators and or not 

# for character in "for loops":
  # print(character)

# range() returns a sequence of numbers
# range(start, stop)
# range(start, stop, increment/decrement)

# advanced control flow --> nested for and while loops
for i in range(1, 3): #1, 2
  for j in range(20, 23): #20, 22
    for k in range(-1, -3, -1): #-1, -2
      print(i * j * k)

# continue -- used to continue to the next iteration (skips)
# break -- breaking the loop that it is in and flows the program to the next part 
# pass -- simply a placeholder that does nothing 

