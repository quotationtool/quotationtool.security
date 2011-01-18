import unittest
import doctest
from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig

import quotationtool.security


def testZCML(test):
    """

        >>> XMLConfig('configure.zcml', quotationtool.security)()

    """


def test_suite():
    return unittest.TestSuite((
            doctest.DocTestSuite(setUp = setUp, tearDown = tearDown),
            ))
