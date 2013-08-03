from nose.tools import *
from nginxgraph.nginxgraph import Nginxgraph
from StringIO import StringIO
import mock #?


class Nginxgraph_tests(self):

    def setUp(self):
        test_file = StringIO()
        test_file.write('031.513.124.312 - - [12/Jul/2013:15:00:11 +0000]\
         "CONNECT mattscodecave.com:443 HTTP/1.1" 400 172 "-" "-"\n\
         99.12.124.12 - - [12/Jul/2013:15:00:14 +0000] "\\x04\\x01\\x00P>\\xE\
         Cl\\xC80\\x00" 400 172 "-" "-"\n10.0.0.1 - - [25/Jun/2013:08:00:21\
          +0000] "GET /w00tw00t.at HTTP/1.1"\
           301 184 "-" "bebs"\n123.123.511.123 - - [25/Jun/2013:11:00:41 +0000]\
            "GET /assets/styles-yo.css HTTP/1.1" 200 3623 "-" "UserAgent \n')

        self.test_line = '123.123.511.123 - - [25/Jun/2013:11:00:41 +0000]\
            "GET /assets/styles-yo.css HTTP/1.1" 200 3623 "-" "UserAgent \n'

        self.parser = Nginxgraph(test_file)

    def test_getIP(self):
        self.parser.getIP

    def test_getGeo(self):
        pass

    def test_get_time(self):
        pass

    def test_get_request_type(self):
        pass

    def test_get_request_response(self):
        pass

    def test_get_request_path(self):
        pass

    def test_get_reply_size(self):
        pass

    def test_get_user_agent(self):
        pass

    def test_output_row(self):
        pass

