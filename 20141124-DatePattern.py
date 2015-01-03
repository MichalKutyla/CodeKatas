__author__ = 'SG0220823'

import unittest
import datetime


class DatePattern(object):
    def __init__(self, year, month, day, weekday=0):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday


    def yearMatches(self, date):        
        return self.fieldMatches(self.year, date.year)

    def monthMatches(self, date):
        return self.fieldMatches(self.month, date.month)

    def dayMatches(self, date):
        return self.fieldMatches(self.day, date.day)

    def weekdayMatches(self, date):
        return self.fieldMatches(self.weekday, date.weekday())

    def fieldMatches(self, patternField, inputField):
        return patternField == inputField or not patternField

    def matches(self, date):
        return (self.yearMatches(date) and
                self.monthMatches(date) and
                self.dayMatches(date) and
                self.weekdayMatches(date))


class DataPatternTests(unittest.TestCase):
    def testMatches(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2004, 9, 28)
        self.failUnless(p.matches(d))

    def testDoesntMatch(self):
        p = DatePattern(2004, 9, 28)
        d = datetime.date(2003, 9, 28)
        self.failIf(p.matches(d))

    def testMatchesYearAsWildCard(self):
        p = DatePattern(0, 9, 28)
        d = datetime.date(2003, 9, 28)
        self.failUnless(p.matches(d))

    def testMatchesYearAndMonthAsWildCards(self):
        p = DatePattern(0, 0, 28)
        d = datetime.date(2003, 9, 28)
        self.failUnless(p.matches(d))

    def testMatchesYearAndMonthAndDayAsWindCards(self):
        p = DatePattern(0, 0, 0)
        d = datetime.date(2003, 9, 28)
        self.failUnless(p.matches(d))

    def testMatchesWeekday(self):
        p = DatePattern(0, 0, 0, 2)
        d = datetime.date(2004, 9, 29)
        self.failUnless(p.matches(d))


def main():
    unittest.main()


if __name__ == '__main__':
    main()



