# Base File to Start Project - Python

# Choose and open file
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

# Auxiliary Variables
count = 0
aux_dict = {}

# For loop to create dictionary with number of occurrences for each From email
for line in fh:
    if line.startswith('From '):
        l_line = line.split()
        key_info = l_line[1]
        if key_info not in aux_dict:
            aux_dict[key_info] = 1
        else:
            value = aux_dict[key_info]
            aux_dict[key_info] = value + 1
    else:
        continue

# Print Result
print(aux_dict)

