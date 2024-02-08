#short = 0   
#medium = 1
#long = 2

#print("Do you want a short, medium or long header?")
#header = input()

import csv
tsv_file = 'mit_conversion.tsv'
fasta_file = 'all_mit_1_copy.fasta'

def read_tsv(tsv_file):
    """Reads the TSV file and returns a dictionary mapping original headers to new descriptions."""
    mapping = {}
    with open(tsv_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) >= 2:
                mapping[row[0]] = row[1]
            else:
                print(f"Ignoring malformed row: {row}")
            
    return mapping

def convert_fasta(fasta_file, mapping):
    """Converts the headers of the FASTA file based on the provided mapping."""
    with open(fasta_file, 'r') as file:
        lines = file.readlines()

    converted_lines = []
    for line in lines:
        if line.startswith('>'):
            header = line.strip().lstrip('>')
            if header in mapping:
                new_header = mapping[header]
                converted_lines.append(f'>{new_header}\n')
            else:
                converted_lines.append(line)
        else:
            converted_lines.append(line)

    with open(fasta_file, 'w') as file:
        file.writelines(converted_lines)


mapping = read_tsv(tsv_file)
convert_fasta(fasta_file, mapping)



