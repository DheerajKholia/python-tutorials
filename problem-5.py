# Find the longest palindrome
import time
file_obj = open(r'C:\Users\dheer\dev\pw-data-science\python-tutorials\data\sowpods.txt')
#print(dir(file_obj))
words = file_obj.readlines()
file_obj.close()

clean_word = [word.strip() for word in words]
tick = time.time()
max_len = 0


for word in clean_word:
    if word == word[::-1]:
        if len(word) > max_len:
            longest_palindrome = word
            max_len =len(word)
print(longest_palindrome)

print(time.time()- tick)