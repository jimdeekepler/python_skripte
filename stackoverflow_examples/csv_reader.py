import csv

def csv_input(filename):

    print(f'Currently reading the annotations from {filename}')

    try:
        csv_input_file = open(filename, 'rt')
    except FileNotFoundError:
        program_help()
        print("[Error] Input File not found")

    csv_reader = csv.reader(csv_input_file, delimiter=',')
    # unfiltered_annots = list([float(i) for i in map(list, csv_reader)])
    # unfiltered_annots = [print(i) for i in map(list, csv_reader)]
    unfiltered_annots = [list(map(float, l)) for l in csv_reader]
    csv_input_file.close()

    return unfiltered_annots

def main():
    print(csv_input('csv_example.csv'))

main()

