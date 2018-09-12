###############################################################################
#
# Tests for libxlsxwriter.
#
# Copyright 2014-2018, John McNamara, jmcnamara@cpan.org
#

import base_test_class

class TestCompareXLSXFiles(base_test_class.XLSXBaseTest):
    """
    Test file created with libxlsxwriter against a file created by Excel.

    """

    def test_chartsheet01(self):
        self.run_exe_test('test_chartsheet01')

    def test_chartsheet02(self):
        self.run_exe_test('test_chartsheet02')

    def test_chartsheet03(self):
        self.run_exe_test('test_chartsheet03')
