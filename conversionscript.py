import sys

def read_fasta(file_path):
    sequences = {}
    current_header = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_header = line[1:]
                sequences[current_header] = ''
            else:
                sequences[current_header] += line
    return sequences

def read_conversion_table(file_path):
    conversion_table = {}
    with open(file_path, 'r') as file:
        for line in file:
            short, medium, long, _ = line.strip().split('\t')
            conversion_table[short] = {'medium': medium, 'long': long}
    return conversion_table

def change_headers(fasta_sequences, conversion_table, header_type):
    changed_sequences = {}
    for header, sequence in fasta_sequences.items():
        short_header = header.split()[0]
        if short_header in conversion_table:
            if header_type in conversion_table[short_header]:
                new_header = conversion_table[short_header][header_type] + ' ' + ' '.join(header.split()[1:])
                changed_sequences[new_header] = sequence
            else:
                changed_sequences[header] = sequence
        else:
            changed_sequences[header] = sequence
    return changed_sequences

def write_fasta(changed_sequences, output_file):
    with open(output_file, 'w') as file:
        for header, sequence in changed_sequences.items():
            file.write('>' + header + '\n')
            file.write(sequence + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python my_code.py FASTA.fasta CONV_TABLE.txt <header_type>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    conv_table_file = sys.argv[2]
    header_type = sys.argv[3]

    if header_type not in ['short', 'medium', 'long']:
        print("<header_type> must be one of 'short', 'medium', or 'long'")
        sys.exit(1)

    fasta_sequences = read_fasta(fasta_file)
    conversion_table = read_conversion_table(conv_table_file)
    changed_sequences = change_headers(fasta_sequences, conversion_table, header_type)
    write_fasta(changed_sequences, "changed_FASTA.fasta")

    print("FASTA file with {} headers has been created.".format(header_type))




