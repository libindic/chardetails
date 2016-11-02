#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testtools import TestCase

from ..core import getInstance


class CharDetailsTest(TestCase):

    def setUp(self):
        super(CharDetailsTest, self).setUp()
        self.instance = getInstance()

    def test_english(self):
        self.assertEqual(self.instance.getdetails(u'AB')[u'A']['HTML Entity'],
                         '65')
