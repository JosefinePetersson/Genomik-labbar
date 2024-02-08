

import sys

def read_conversion_table(conv_table_file):
    conv_table = {}
    with open(conv_table_file, 'r') as f:
        for line in f:
            short, medium, long, _ = line.strip().split('\t')
            conv_table[short] = {'short': short, 'medium': medium, 'long': long}
    return conv_table

def modify_header(header, conv_table, header_type):
    header_parts = header.split()
    short_header = header_parts[0]
    if short_header in conv_table:
        return conv_table[short_header][header_type] + ' ' + ' '.join(header_parts[1:])
    return header

def modify_fasta(fasta_file, conv_table, header_type):
    modified_lines = []
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                modified_header_line = modify_header(line.strip()[1:], conv_table, header_type)
                modified_lines.append('>' + modified_header_line + '\n')
            else:
                modified_lines.append(line)
    return modified_lines

def main():
    if len(sys.argv) != 3:
        print("Usage: python my_code.py FASTA.fasta CONV_TABLE.txt")
        return

    fasta_file = sys.argv[1]
    conv_table_file = sys.argv[2]

    conv_table = read_conversion_table(conv_table_file)

    print("Choose header type: (short, medium, long)")
    header_type = raw_input().lower()
    while header_type not in ['short', 'medium', 'long']:
        print("Invalid header type. Choose from short, medium, long:")
        header_type = raw_input().lower()

    modified_content = modify_fasta(fasta_file, conv_table, header_type)
    for line in modified_content:
        print(line.strip())

if __name__ == "__main__":
    main()
