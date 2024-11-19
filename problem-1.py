#Find all the words which contains 'UU' in the word
# file_obj = open('C:\\Users\\dheer\\dev\\pw-data-science\\python-tutorials\\data\\sowpods.txt')
file_obj = open(r'C:\Users\dheer\dev\pw-data-science\python-tutorials\data\sowpods.txt')
#print(dir(file_obj))
words = file_obj.readlines()
# print(words)
# normal way
for word in words:
    if 'UU' in word:
        print(word)

#list comprehension way
# print([word for word in words if 'UU' in word])

file_obj.close()
