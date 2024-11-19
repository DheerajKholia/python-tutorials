# print all the palindrome


import time
file_obj = open(r'C:\Users\dheer\dev\pw-data-science\python-tutorials\data\sowpods.txt')
#print(dir(file_obj))
words = file_obj.readlines()
file_obj.close()

clean_word = [word.strip() for word in words]
tick = time.time()

for word in clean_word:
    if word == word[::-1]:
        print(word)

print(time.time()- tick)