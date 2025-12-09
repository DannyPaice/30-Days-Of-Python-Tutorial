

# Syntax for opening files
'''
open('filename', mode) where mode is (r, a, w, x, t, b)
r - read
a - append
w - write
x - create
t - text
b - binary
'''


# Opening files for reading ~ default mode is already r
f = open("Day_19-Modules/example.txt")
txt = f.read(5) # reads the first 5 indexes
print(txt)
f.close()

# readline(): read only the first line
f = open("Day_19-Modules/example.txt")
line = f.readline()
print(line)
f.close()

# readlines(): read all the text line by line and return a list of lines
f = open("Day_19-Modules/example.txt")
lines = f.readlines()
print(lines) # output a list
f.close()



# with method ~ automatically closes the file
with open("Day_19-Modules/example.txt") as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)



# opening files for writing and updating
with open("Day_19-Modules/example2.txt", "a") as f:
    f.write('This text has to be appended at the end')

with open("Day_19-Modules/example2.txt", "a") as f:
    f.write('\nThis is the extention of example2') #check example2.txt





