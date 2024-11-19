# Print all alphabets that never appear double
# e.g if AA is there in any words it shouldn't qualify for output
# if QQ is not there in any of the words,  print the alphabet

import time
file_obj = open(r'C:\Users\dheer\dev\pw-data-science\python-tutorials\data\sowpods.txt')
#print(dir(file_obj))
words = file_obj.readlines()
file_obj.close()

tick = time.time()
for alpha in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    flag = True
    for word in words:
        if alpha*2 in word:
            flag = False
            break
    if flag == True:
        print(alpha)
        


print(time.time()- tick)