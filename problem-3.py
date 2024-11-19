# English words that contains all the vowels

import time
file_obj = open(r'C:\Users\dheer\dev\pw-data-science\python-tutorials\data\sowpods.txt')
#print(dir(file_obj))
words = file_obj.readlines()
file_obj.close()

tick = time.time()
vowel = 'AEIOU'
for word in words:
    flag = True
    for v in vowel:
        if v not in word:
            flag = False
            break
    if flag == True:
        print(word)

print(time.time()- tick)