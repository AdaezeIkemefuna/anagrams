# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(first_word, second_word):

     #uniform cases and removing spaces
     first = first_word.lower().replace(" ", "")
     second = second_word.lower().replace(" ", "")

     #converting to list and sorting
     first_list = list(first)
     first_list.sort()
     
     second_list = list(second)
     second_list.sort()

     return first_list == second_list

#examples of true
print(find_anagrams("Ada eze", "ezeada"))
print(find_anagrams("listen", "silent"))

#example of false
print(find_anagrams("rockstar", "rockster"))
print(find_anagrams("sensual", "sensuous"))




