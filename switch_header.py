with open('mit_conversion.tsv', 'r') as mit_conversion:
    lines = mit_conversion.readlines()

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

with open('Mit/all_mit.fasta', 'r') as file:
    seqs = file.readlines()
with open('Mit/all_mit.fasta', 'w') as out_file:

    for seq in seqs:
        if seq.startswith('>'):
            for row_index, row in enumerate(data):
                    #print(row)
                    if str(seq[1:-1]) in row:
                        for col_index, value in enumerate(row):
                              if header == col_index:
                                out_file.write('>'+value+'\n')

        else:
            out_file.write(seq)


