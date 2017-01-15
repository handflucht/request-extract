import re
import requests


def execute_regex(url, pattern, group_name, multiline=False):
    request = requests.get(url)

    if group_name is None:
        group_name = 0

    if multiline:
        matches = re.finditer(pattern, request.text, re.MULTILINE)

        return [m.group(group_name) for m in matches]
    else:
        pattern = re.compile(pattern)
        matches = pattern.search(request.text)

        return [matches.group(group_name)]

