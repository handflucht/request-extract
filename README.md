# Introduction
Executes an regular expression on a given url and returns the result.

## Installation

`pip3 install git+https://github.com/handflucht/response-extract.git`

## Usage

```
python3 bin/main.py --help
usage: main.py [-h] --url URL [--regex REGEX] [--regex_group REGEX_GROUP]
               [--regex_ml] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             url to call
  --regex REGEX         regex to execute
  --regex_group REGEX_GROUP
                        named regex group to return
  --regex_ml            use multiline
  -v, --verbose         write additional output
```

## Example

Get all sentences from `The New York Times` where the word `Trump` appears:
```
python3 bin/main.py --url http://www.nytimes.com  --regex '(?P<sentence>([\w+ ,\"])+Trump[\w+ .,\"]+[\.])' --regex_group sentence
[' Distrust of Hillary Clinton and a liking for Ivanka Trump also helped.']
```
