#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode Character Details
# Copyright 2008-2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email:
# santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in

import os
import unicodedata

__all__ = ['CharDetails', 'getInstance']


class CharDetails:
    """
    Shows the Unicode Character Details of a given character
    """

    def getdetails(self, text):
        """
        Gives details of all charecters in the given string.

        :param text: The unicode string to be examined.
        :type text: str.
        :returns:  dictionary with details.

        ::

         >>> import chardetails.getInstance
         >>> a = getInstance()
         >>> a.getdetails(u"run")
         {'Characters': [u'r', u'u', u'n'],
         u'n': {'AlphaNumeric': 'True',
         'Alphabet': 'True',
         'Canonical Decomposition': '',
         'Code point': "u'n'",
         'Digit': 'False',
         'HTML Entity': '110',
         'Name': 'LATIN SMALL LETTER N'},
         u'r': {'AlphaNumeric': 'True',
         'Alphabet': 'True',
         'Canonical Decomposition': '',
         'Code point': "u'r'",
         'Digit': 'False',
         'HTML Entity': '114',
         'Name': 'LATIN SMALL LETTER R'},
         u'u': {'AlphaNumeric': 'True',
         'Alphabet': 'True',
         'Canonical Decomposition': '',
         'Code point': "u'u'",
         'Digit': 'False',
         'HTML Entity': '117',
         'Name': 'LATIN SMALL LETTER U'}}


        """
        chardetails = {}
        for character in text:
            chardetails[character] = {}
            chardetails[character]['Name'] = unicodedata.name(character)
            chardetails[character]['HTML Entity'] = str(ord(character))
            chardetails[character]['Code point'] = repr(character)
            try:
                chardetails[character]['Numeric Value'] = \
                    unicodedata.numeric(character)
            except:
                pass
            try:
                chardetails[character]['Decimal Value'] = \
                    unicodedata.decimal(character)
            except:
                pass
            try:
                chardetails[character]['Digit'] = unicodedata.digit(mychar)
            except:
                pass
            chardetails[character]['Alphabet'] = str(character.isalpha())
            chardetails[character]['Digit'] = str(character.isdigit())
            chardetails[character]['AlphaNumeric'] = str(character.isalnum())
            chardetails[character]['Canonical Decomposition'] = \
                unicodedata.decomposition(character)

        chardetails['Characters'] = list(text)
        return chardetails

    def get_module_name(self):
        """Returns modules Name """
        return "Unicode Character Details"

    def get_info(self):
        """ Gives Info on the module """
        return "Shows the Unicode Character Details of a given character"


def getInstance():
    """Returns an instance of :class:`CharDetails` class."""
    return CharDetails()
