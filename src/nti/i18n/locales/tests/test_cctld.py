#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for locale data.
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

import unittest

from zope.component.testlayer import ZCMLFileLayer
from zope import component

import nti.i18n
from nti.i18n.locales.interfaces import ICcTLDInformation


class TestConfiguredTLDUtility(unittest.TestCase):

    layer = ZCMLFileLayer(nti.i18n, zcml_file='configure.zcml')

    def test_full_domain_list(self):
        info = component.getUtility(ICcTLDInformation)
        available = info.getAvailableTLDs()
        with_lang = info.getTLDs()
        for cc in available:
            self.assertIn(cc, with_lang)

        self.assertEqual(["en"], info.getLanguagesForTLD('us'))

        # Bad tlds
        self.assertRaises(KeyError, info.getLanguagesForTLD, __name__)
