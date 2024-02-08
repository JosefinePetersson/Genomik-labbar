import sys

def read_fasta(filename):
    fasta_dict = {}
    with open(filename, 'r') as f:
        header = None
        sequence = ""
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header is not None:
                    fasta_dict[header] = sequence
                header = line[1:]
                sequence = ""
            else:
                sequence += line
        if header is not None:
            fasta_dict[header] = sequence
    return fasta_dict

def read_conv_table(filename):
    conv_table = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                fields = line.split('\t')
                if len(fields) >= 3:
                    short_name = fields[0]
                    medium_name = fields[1]
                    long_name = fields[2].strip()  # Strip leading and trailing whitespace
                    conv_table[long_name] = {'short': short_name, 'medium': medium_name}
    return conv_table



def convert_header(header, conv_table, mode):
    if mode == 'short':
        if header in conv_table and 'short' in conv_table[header]:
            print("Converting %s to short header: %s" % (header, conv_table[header]['short']))
            return conv_table[header]['short']
        else:
            print("No short header found for %s" % header)
            return header
    elif mode == 'medium':
        if header in conv_table and 'medium' in conv_table[header]:
            print("Converting %s to medium header: %s" % (header, conv_table[header]['medium']))
            return conv_table[header]['medium']
        else:
            print("No medium header found for %s" % header)
            return header
    elif mode == 'long':
        print("Using long header: %s" % header)
        return header
    else:
        return header


def main():
    if len(sys.argv) != 4:
        print("Usage: python conversionscript.py FASTA.fasta CONV_TABLE.txt [short|medium|long]")
        sys.exit(1)

    fasta_filename = sys.argv[1]
    conv_table_filename = sys.argv[2]
    mode = sys.argv[3]

    fasta_dict = read_fasta(fasta_filename)
    conv_table = read_conv_table(conv_table_filename)

    print("Headers from FASTA file:")
    for header in fasta_dict.keys():
        print(header)

    print("\nHeaders from conversion table:")
    for header in conv_table.keys():
        print(header)

    for header, sequence in fasta_dict.items():
        new_header = convert_header(header, conv_table, mode)
        print(">%s" % new_header)
        print(sequence)


if __name__ == "__main__":
    main()


