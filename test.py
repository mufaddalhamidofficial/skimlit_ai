# Write to a file

with open('test.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('How are you?\n')
    file.write('I am fine.\n')
    file.write('Goodbye.')
    
# Reading the file
with open('test.txt', 'r') as file:
    print(file.read())