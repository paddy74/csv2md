import sys
import csv


def csv_to_table(file, delimiter=',', quotechar='"'):
    return list(csv.reader(file, delimiter=delimiter, quotechar=quotechar))


def get_table_widths(table):
    table_lengths = [[len(cell) for cell in row] for row in table]
    return list(map(max, zip(*table_lengths)))


def table_to_md(table):
    table_widths = get_table_widths(table)

    md_table = ['| ' + ' | '.join([cell.ljust(width) for cell, width in zip(row, table_widths)]) + ' |'
                for row in table]

    md_table.insert(1, '| ' + ' | '.join(['-' * width for width in table_widths]) + ' |')

    return '\n'.join(md_table)


def main(args):
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
