import argparse
from gendiff.modules.difference import generate_diff


def main(path1, path2):
    print(generate_diff(path1, path2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration file and shows a difference')
    parser.add_argument('-ff', '--first_file', type=str)
    parser.add_argument('-s', '--second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output'
    )
    args = parser.parse_args()
    main(args.first_file, args.second_file)
