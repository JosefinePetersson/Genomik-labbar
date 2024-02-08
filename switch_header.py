import re


with open('Mit_conversion.tsv', 'r') as cytB_conversion:
    lines = cytB_conversion.readlines()

data = []

# Split each line into columns and store in the data list
for line in lines:
    columns = line.strip().split('    ')
    data.append(columns)

input = input('State which header is wished for: short, medium or long: ')
if input =='short':
    header = 0
elif input == 'medium':
    header = 1
elif input == 'long':
    header = 2
else:
    print('Please rerun and specify exactly short, medium or long')

with open('Mit/all_mit_1.fasta', 'r') as file:
    seq = file.readlines()

    # for line in data:
    #     if re.search(r'>', line):
    #         print(line)
   

for row_index, row in enumerate(data):
    for col_index, value in enumerate(row):
        if col_index == header:
            print(value)

