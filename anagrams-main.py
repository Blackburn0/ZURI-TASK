# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(string_one, string_two):
    # [assignment] Add your code here
    if sorted(string_one) == sorted(string_two):
        return True
    else:
        return False


print(find_anagrams("evil", "vile"))

