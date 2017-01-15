import argparse

from responseextract import extract


def main(args):
    print(extract.execute_regex(args.url, args.regex, args.regex_group, args.regex_ml))

if __name__ == '__main__':
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--url', help='url to call', required=True)
    arguments.add_argument('--regex', help='regex to execute')
    arguments.add_argument('--regex_group', help='named regex group to return')
    arguments.add_argument('--regex_ml', help='use multiline', action='store_true')
    arguments.add_argument('-v', '--verbose', help='write additional output', action='store_true')

    main(arguments.parse_args())
