# Shakespear words that do not appear in modern dictionary
# words that are in sonnet_words.txt and not in sowpods.txt

import time

file_obj1 = open(r'C:\Users\dheer\dev\pw-data-science\python-tutorials\data\sowpods.txt')
sowpods_words = file_obj1.readlines()

file_obj2 = open(r'C:\Users\dheer\dev\pw-data-science\python-tutorials\data\sonnet_words.txt')
sonnet_words = file_obj2.readlines()

file_obj1.close()
file_obj2.close()

sowpods_words = {word.strip() for word in sowpods_words} # using set reduces the time to compare
sonnet_words = [word.strip() for word in sonnet_words]

tick = time.time()
for word in sonnet_words:
    if word not in sowpods_words:
        print(word)
print(time.time() - tick)