import argparse


def main():
	print('Hello!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration file and shows a difference')
    parser.add_argument('fist_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output'
    )
    args = parser.parse_args()
    main()
