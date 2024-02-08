import sys

def read_conversion_table(conv_table_file):
    conv_table = {}
    with open(conv_table_file, 'r') as file:
        for line in file:
            short, medium, long, _ = line.strip().split('\t')
            conv_table[short] = {'short': short, 'medium': medium, 'long': long}
    return conv_table

def convert_headers(fasta_file, conv_table, header_type):
    converted_lines = []
    with open(fasta_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                parts = line.strip().split(' ')
                header = parts[0][1:]
                header_key = header.split()[0]  # Extracting the key part of the header
                if header_key in conv_table:
                    if header_type == 'short':
                        new_header = conv_table[header_key]['short']
                    elif header_type == 'medium':
                        new_header = conv_table[header_key]['medium']
                    elif header_type == 'long':
                        new_header = conv_table[header_key]['long']
                    else:
                        new_header = header
                    parts[0] = '>' + new_header
                    converted_lines.append(' '.join(parts) + '\n')
                else:
                    converted_lines.append(line)
            else:
                converted_lines.append(line)
    return converted_lines

def write_output(output_file, converted_lines):
    with open(output_file, 'w') as file:
        for line in converted_lines:
            file.write(line)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python my_code.py FASTA.fasta CONV_TABLE.txt [short|medium|long]")
        sys.exit(1)

    fasta_file = sys.argv[1]
    conv_table_file = sys.argv[2]
    header_type = sys.argv[3]

    if header_type not in ['short', 'medium', 'long']:
        print("Invalid header type. Please choose from 'short', 'medium', or 'long'.")
        sys.exit(1)

    conv_table = read_conversion_table(conv_table_file)
    converted_lines = convert_headers(fasta_file, conv_table, header_type)
    output_file = fasta_file.split('.')[0] + '_' + header_type.upper() + '.fasta'
    write_output(output_file, converted_lines)
    print("Conversion completed. Output saved to", output_file)

