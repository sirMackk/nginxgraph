from nose.tools import *
from nginxgraph.nginxgraph import Nginxgraph
from StringIO import StringIO
import mock #?


class Nginxgraph_tests(object):

    def setUp(self):
        test_file = StringIO()
        test_file.write('93.184.216.119 - - [12/Jul/2013:15:00:11 +0000]\
         "CONNECT mattscodecave.com:443 HTTP/1.1" 400 172 "-" "-"\n\
         99.12.124.12 - - [12/Jul/2013:15:00:14 +0000] "\\x04\\x01\\x00P>\\xE\
         Cl\\xC80\\x00" 400 172 "-" "-"\n93.184.216.119 - - [25/Jun/2013:08:00:21\
          +0000] "GET /w00tw00t.at HTTP/1.1"\
           301 184 "-" "bebs"\n93.184.216.119 - - [25/Jun/2013:11:00:41 +0000]\
            "GET /assets/styles-yo.css HTTP/1.1" 200 3623 "-" "UserAgent \n')

        self.test_line = '93.184.216.119 - - [25/Jun/2013:11:00:41 +0000]\
            "GET /assets/styles-yo.css HTTP/1.1" 200 3623 "-" "Mozilla/5.0\
             (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
              Chrome/28.0.1500.72 Safari/537.36\n'

        self.nginxgraph = Nginxgraph() #nah, has to be a better wai

    def test_get_geo_ip(self):
        geo_info = self.nginxgraph.get_geo_IP(self.test_line)
        geo_info_parsed = ['93.184.216.119', 'United States', 'US', '']
        assert_equal(geo_info, geo_info_parsed)

    def test_get_time(self):
        date = self.nginxgraph.get_time(self.test_line)
        assert_equal(date, '25/Jun/2013:11:00:41')

    def test_get_request_type(self):
        request_type = self.nginxgraph.get_request_type(self.test_line[25:])
        assert_equal(request_type, 'GET')
        #expand to include more intricate requests or lack of request

    def test_get_request_response(self):
        request_response = self.nginxgraph.get_request_response(self.test_line[25:])
        assert_equal(request_response, '200')

    def test_get_request_path(self):
        request_path = self.nginxgraph.get_request_path(self.test_line[25:])
        assert_equal(request_path, '/assets/styles-yo.css')
        #expand to checkout more path types

    def test_get_reply_size(self):
        reply_size = self.nginxgraph.get_reply_size(self.test_line)
        assert_equal(reply_size, '3623')

    def test_get_user_agent(self):
        request_u_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72\
          Safari/537.36'
        u_agent = self.nginxgraph.get_user_agent(self.test_line)
        assert_equal(u_agent, request_u_agent)

    # def test_output_row(self):
    #     pass

