import requests
import argparse
import re


def execute_match(url, pattern, group_name, multiline=False):
    request = requests.get(url)

    if multiline:
        matches = re.finditer(pattern, request.text, re.MULTILINE)

        return [m.group(group_name) for m in matches]
    else:
        pattern = re.compile(pattern)
        matches = pattern.search(request.text)
        return [matches.group(group_name)]


def main(args):
    print(execute_match(args.url, args.regex, args.regex_group, args.regex_ml))


if __name__ == '__main__':
    arguments = argparse.ArgumentParser()
    arguments.add_argument('--url', help='url to call', required=True)
    arguments.add_argument('--regex', help='regex to execute', required=True)
    arguments.add_argument('--regex_group', help='named regex group to return', required=True)
    arguments.add_argument('--regex_ml', help='use multiline', action='store_true')
    arguments.add_argument('-v', '--verbose', help='write additional output', action='store_true')

    main(arguments.parse_args())
