from unittest import TestCase

from sqf.types import Statement, Array, Boolean, Code, Nothing, \
    Variable as V, Number as N
from sqf.keywords import Keyword


class TestTypesToString(TestCase):

    def test_bool(self):
        self.assertEqual('true', str(Boolean(True)))
        self.assertEqual('false', str(Boolean(False)))

    def test_number(self):
        self.assertEqual('1', str(N(1)))
        self.assertEqual('1.10', str(N(1.1)))

    def test_array(self):
        self.assertEqual('[1,1]', str(Array([1, 1])))

    def test_reservedtoken(self):
        self.assertEqual('for', str(Keyword('for')))

    def test_nothing(self):
        self.assertEqual('Nothing', str(Nothing))

    def test_code(self):
        self.assertEqual('{_x=2;}', str(Code([Statement([V('_x'), Keyword('='), N(2)], ending=True)])))
