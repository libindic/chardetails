# LibIndic Chardetails


[![Build Status](https://travis-ci.org/libindic/chardetails.svg?branch=master)](https://travis-ci.org/libindic/chardetails)
[![Coverage Status](https://coveralls.io/repos/github/libindic/chardetails/badge.svg?branch=master)](https://coveralls.io/github/libindic/chardetails?branch=master)


LibIndic's chardetails module may be used to get the details of a given unicode
character.

## Installation
1. Clone the repository `git clone https://github.com/libindic/chardetails.git`
2. Change to the cloned directory `cd chardetails`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/chardetails*.tar.gz`

## Usage
```
Input: String of Unicode characters
Output: Dictionary containing details of each character

>>> from libindic.chardetails import getInstance
>>> tool = getInstance()
>>> tool.getdetails(u'ആന')

{'Characters': [u'\u0d06', u'\u0d28'],
 u'\u0d06': {'AlphaNumeric': 'True',
  'Alphabet': 'True',
  'Canonical Decomposition': '',
  'Code point': "u'\\u0d06'",
  'Digit': 'False',
  'HTML Entity': '3334',
  'Name': 'MALAYALAM LETTER AA'},
 u'\u0d28': {'AlphaNumeric': 'True',
  'Alphabet': 'True',
  'Canonical Decomposition': '',
  'Code point': "u'\\u0d28'",
  'Digit': 'False',
  'HTML Entity': '3368',
  'Name': 'MALAYALAM LETTER NA'}}
```

For more details read the [docs](http://indicstemmer.rtfd.org/)

## Running tests
To run tests, 

```
cd chardetails
python setup.py test
```
