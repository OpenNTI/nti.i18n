# -*- coding: utf-8 -*-
"""
Interfaces related to localization.

"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"


from zope.interface import Interface

try:
    from plone.i18n.locales.interfaces import ICountryAvailability as _ICountryAvailability
except ImportError:
    # Not on Py3
    _ICountryAvailability = Interface

class ICountryAvailability(_ICountryAvailability):
    """A list of available coutries."""

    def getAvailableCountries():
        """
        Return a sequence or view of unicode country tags for available
        countries.
        """

    def getCountries():
        """
        Return a dictionary mapping country tags to country data.

        Country data has at least the 'name' key.
        """

    def getCountryListing():
        """
        Return a sequence of unicode country code and country name tuples.
        """
