from nose.tools import *
from nginxgraph.statfile import StatFile
import json
import os

class StatFile_tests(object):

    def setUp(self):
        self.TEST_FILE_NAME = 'test_file'
        self.s_file = StatFile(self.TEST_FILE_NAME)
        self.test_row = ['0.0.0.0', 'United States', 'Brooklyn', '4/7/1776',
                 'GET', '200', '100', '200', '/', 'Mozilla/5.0 (X11' \
                '; Linux x86_64) AppleWebKit/537.22 (KHTML. like Geck' \
                'o) Ubuntu Chromium/25.0.1364.160 Chrome/25.0.1364.160' \
                ' Safari/537.22']
        self.s_file.append_to_list(self.test_row)
        self.s_file.append_to_list(self.test_row)

    def tearDown(self):
        if os.path.isfile(self.TEST_FILE_NAME + '.csv'): os.unlink(self.TEST_FILE_NAME + '.csv')
        if os.path.isfile(self.TEST_FILE_NAME + '.js'): os.unlink(self.TEST_FILE_NAME + '.js')

    def test_init(self):
        assert_true(isinstance(self.s_file.master_list, list))

    def test_append_to_list(self):
        assert_equal(len(self.s_file.master_list), 2)
        assert_equal(self.s_file.master_list[0], self.test_row)
        assert_equal(self.s_file.master_list[1], self.test_row)

    def test_write_csv(self):
        self.s_file.write_csv()
        test_file = open(self.TEST_FILE_NAME + '.csv', 'rb')
        lines = test_file.readlines()
        assert_equal(len(lines), 2)
        assert_equal(lines[0], ','.join(self.test_row) + '\n')
        test_file.close()

    def test_write_json(self):
        self.s_file.write_json()
        test_file = open(self.TEST_FILE_NAME + '.js', 'rb')
        assert_equal(test_file.readline(), json.dumps([dict(zip(self.s_file.log_key, i))
                                             for i in self.s_file.master_list]))
        test_file.close()

    def test_csv_popular_column(self):
        self.s_file.csv_popular_column(0)
        test_file = open(self.TEST_FILE_NAME + '.csv', 'rb')
        assert_equal(test_file.readline(), '0.0.0.0,2\n')
        test_file.close()

    def test_json_popular_column(self):
        self.s_file.json_popular_column(0)
        test_file = open(self.TEST_FILE_NAME + '.js', 'rb')
        assert_equal(test_file.readline(), '[{"value": 2, "key": "0.0.0.0"}]')
        test_file.close()