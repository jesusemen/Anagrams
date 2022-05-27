# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
    str1 = ''
    str2 = ''
    strg1 = sorted(str1)
    strg2 = sorted(str2)
    
    if strg1 == strg2:
        if len(str1) == len(str2):
           return True
        else:
           return False
    else:
           return False
print(find_anagram('earthen ngh', 'heart'))

    