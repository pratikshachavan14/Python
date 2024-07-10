# Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
lst1=[int(i) for i in input("Enter the elements in list 1: ").split(" ")]
lst2=[int(i) for i in input("Enter the elements in list 2: ").split(" ")]

print("List 1")
print(lst1)
print("List 2")
print(lst2)

def overlapping(lst1, lst2):
  for i in lst1:
    for j in lst2:
      if i == j:
        print("Common Element found")
        return True
  else:
    print("No Common Element Found")
    return False

a = overlapping(lst1, lst2)
print(a)

# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
from functools import reduce

lst=[i for i in input("Enter a list of words: ").split(" ")]
lst1=[]
def find_longest_word(lst):
  for i in lst:
    lst1.append(len(i))
  max1=reduce(lambda x,y:x if x>y else y,lst1)
  # return max(lst1)
  return max1

max = find_longest_word(lst)
print("Max= ",max)

# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n
lst=[i for i in input("Enter a list of words: ").split(" ")]
n=int(input("Enter integer: "))
def filter_long_words(lst, n):
  lst2=list(filter(lambda x:len(x)>n, lst))
  #print(lst2)
  return lst2

max = filter_long_words(lst, n)
print("Max= ",max)

# Define a simple "spelling correction" function correct() that takes a string and sees to it that
# 1) two or more occurrences of the space character is compressed into one, and
# 2) inserts an extra space after a period if the period is directly followed by a letter.
# e.g. correct("This is very funny and cool.Indeed!")
# should return "This is very funny and cool. Indeed!"

# str1=input("Enter string: ")
# def correct(str1):
#   while "  " in str1:
#     str1.replace("  ", " ")
#     print(str1)

# correct("This is  very  funny and cool.Indeed!")


str1=input("Enter String: ")
def correct(str1):
  while "  " in str1:
    str1=str1.replace("  "," ")
  str1=str1.replace(".", ". ")
  print(str1)

correct(str1)

# In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A simple set of heuristic rules can be given as follows:
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, change ie to y and add ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding ing
# By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form
# returns its present participle form. Test your function with words such as lie, see, move and hug.

def make_ing_form(word):
  word=word.lower()
  vow=['a','e','i','o','u']

  #If the verb ends in ie, change ie to y and add ing
  if word[-2] == "i" and word[-1] == "e":
    word = word.replace("ie", "ying")
    print(word)

  # If the verb ends in e, drop the e and add ing
  elif word[-1] == "e":
    word = word.replace(word[-1], "ing")
    print(word)

  # For words consisting of consonant-vowel-consonant, double the final letter before adding ing
  elif (word[-3] not in vow) and (word[-2] in vow) and (word[-1] not in vow):
    word = word.replace(word[-1], word[-1]+"ing")
    print(word)

  #default
  else:
    word = word + "ing"
    print(word)


word = input("Enter the word: ")
make_ing_form(word)