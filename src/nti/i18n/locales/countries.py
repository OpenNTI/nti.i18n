# -*- coding: utf-8 -*-
"""
Implementation of country data.


"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

import json
import pkg_resources

from zope.interface import implementer
from zope.cachedescriptors.property import Lazy

from .interfaces import ICountryAvailability

@implementer(ICountryAvailability)
class CountryAvailability(object):
    """
    Default implementation of country availability, based on
    countries.json distributed with this package.
    """

    @Lazy
    def _countrylist(self):
        country_bytes = pkg_resources.resource_string(__name__, 'countries.json')
        country_str = country_bytes.decode('utf-8')
        return json.loads(country_str)

    def getAvailableCountries(self):
        return self._countrylist.keys()

    def getCountries(self):
        return self._countrylist.copy()

    def getCountryListing(self):
        return [(code, data[u'name']) for code, data in self._countrylist.items()]
