#//Demo Example of file handling in Python that demonstrates how to open a file, read its contents, and write to it:

# Opening a file
#file = open('viratt.txt', 'r')

# Reading from a file
#content = file.read()
#print(content)

# Closing a file
#file.close()

# Writing to a file
with open('Pavan.txt', 'a') as file:
    file.write('Python training.')

# Reading from a file again
with open('Pavan1.txt', 'r') as file:
    content = file.read()
    print(content)
