# -*- coding: utf-8 -*-
import os
import unittest

from xlsx import Workbook

class WorkbookTestCase(unittest.TestCase):

    def setUp(self):
        """ Getting all file from fixtures dir """
        self.workbooks = {}
        fixtures_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    'fixtures'))
        xlsx_files = os.listdir(fixtures_dir)
        for filename in xlsx_files:
            self.workbooks[filename] = Workbook(
                os.path.join(fixtures_dir, filename))

    def test_basic(self):
        """ These test will run for all test files """

        for filename, workbook in self.workbooks.items():
            for sheet in workbook:
                assert hasattr(sheet, 'id')
                assert isinstance(sheet.name, basestring)
                assert isinstance(sheet.rows(), dict)
                assert isinstance(sheet.cols(), dict)

                for row_num, cells in sheet.rows().iteritems():
                    assert isinstance(row_num, int)
                    assert isinstance(cells, list)
                    for cell in cells:
                        assert hasattr(cell, 'id')
                        assert hasattr(cell, 'column')
                        assert hasattr(cell, 'row')
                        assert hasattr(cell, 'value')
                        assert cell.row == row_num

    def test_test1(self):
        """ Specific test for `testdata/test1.xslx` file including
        unicode strings and different date formats
        """
        workbook = self.workbooks['test1.xlsx']

        self.assertEqual(unicode(workbook[1].name), u'рускии')
        self.assertEqual(unicode(workbook[2].name), u'性 文化交流 例如')
        self.assertEqual(unicode(workbook[3].name), u'تعد. بحق طائ')

        for row_num, cells in workbook[1].rows().iteritems():
            if row_num == 1:
                self.assertEqual(unicode(cells[0].value), u'лорем ипсум')
                self.assertEqual(unicode(cells[1].value), u'2')
            if row_num == 2: #Test date fields
                self.assertEqual(cells[0].value, (2010, 11, 12, 0, 0, 0))
                self.assertEqual(cells[1].value, (1987, 12, 20, 0, 0, 0))
                self.assertEqual(cells[2].value, (1987, 12, 20, 0, 0, 0))
                self.assertEqual(cells[3].value, (1987, 12, 20, 0, 0, 0))
                break

        # Cell A1 in u'性 文化交流 例如'
        self.assertEqual(unicode(workbook[2].cols()['A'][0].value),
                         u'性 文化交流 例如')
        self.assertEqual(unicode(workbook[2].cols()['A'][1].value),
                         u'エム セシビ め「こを バジョン')

    def test_test3(self):
        '''
        Test handling blank cells
        '''
        workbook = self.workbooks['test3.xlsx']

        # No row 3, contains only blank cells
        self.assertEqual([row for row in workbook[1].rows()], [1, 2, 4])

        # All rows have 5 cells
        for row_num, cells in workbook[1].rows().iteritems():
            self.assertEqual(len([vars(cell) for cell in cells]), 5)

        # direct cell access
        self.assertEqual(
            sorted([cell for cell in workbook[1]]),
            [
                u'A1', u'A2', u'A4',
                u'B1', u'B2', u'B4',
                u'C1', u'C2', u'C4',
                u'D1', u'D2', u'D4',
                u'E1', u'E2', u'E4'
            ]
        )

if __name__ == '__main__':
    unittest.main()
