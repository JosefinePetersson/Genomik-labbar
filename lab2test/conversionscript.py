import sys


def find_fasta_headers(file_path):
    header_idx = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if line.startswith('>'):
                header_idx.append(i)
    return header_idx


def convert_header(header, type, conversion_file):
    header = header[1:].strip()
    type_dict = {'short': 0, 'medium': 1, 'long': 2}

    if type not in type_dict:
        print(f'Error: Invalid type "{type}". Valid types are: {", ".join(type_dict.keys())}')
        return header  # Return original header if type is invalid

    with open(conversion_file, 'r') as f:
        for row in f:
            row = row.strip()
            row = row.split('\t')
            if header in row:
                return '>' + row[type_dict[type]] + '\n'
    print('Error header not in conversion file:', header)
    return header  # Return original header if not found in conversion file


def change_headers(header_idx, type, conversion_file, file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for idx in header_idx:
        lines[idx] = convert_header(lines[idx], type, conversion_file)
    with open(file_path, 'w') as f:
        f.writelines(lines)


def main():
    if len(sys.argv) != 3:
        print('2 arguments needed')
    else:
        file_name = sys.argv[1]
        headertype = sys.argv[2]
        if 'mitochondria' in file_name:
            conversion_file = 'mitochondria_conversion.txt'
        elif 'cytb' in file_name:
            conversion_file = 'cytb_conversion.txt'
        else:
            print('No idea which conversion file to use')
            return
        header_idx = find_fasta_headers(file_name)
        change_headers(header_idx, headertype, conversion_file, file_name)


if __name__ == '__main__':
    main()


