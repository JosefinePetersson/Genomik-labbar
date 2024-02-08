def create_mock_fasta(file_path):
    with open(file_path, 'w') as file:
        file.write(">Header1 mock fasta sequence 1\n")
        file.write("ATCGATCGATCG\n")
        file.write(">Header2 mock fasta sequence 2\n")
        file.write("CGATCGATCGAT\n")

def create_mock_conversion_table(file_path):
    with open(file_path, 'w') as file:
        file.write("APP\tAPPLE\tAPPLES are_nice\textra_column\n")
        file.write("BAN\tBANANA\tBANANAS_arent\textra_info\n")
        file.write("WAT\tWATERMELON\tWATERMELON_is_green\tsome_extra_stuff\n")

if __name__ == "__main__":
    create_mock_fasta("mock_FASTA.fasta")
    create_mock_conversion_table("mock_CONV_TABLE.txt")
