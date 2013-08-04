import re
import pygeoip

class Nginxgraph(object):
    def __init__(self, file_like_object):
        self.file = file_like_object
        try:
          log = open(self.file, 'rb')
        except IOError:
          print "Cannot find input file"
          exit(1)

        lines = log.readlines()
        log.close()

        return analyze_log(lines)

    def analyze_log(self, lines):
        """
        main log analysis function composed of smaller
        functions targeting specific parts of the log
        """
        data = []
        for val in lines:
            row = []
            row += self.get_geo_ip(val)
            row += self.get_time(val)

            remainder = val[30:]
            row += self.get_request_type(remainder)
            row += self.get_request_response(remainder)
            row += self.get_reply_size(remainder)

            row += self.get_request_path(remainder)
            row += self.get_user_agent(i)
          
            data.append(row)

        return data

    def get_geo_ip(self, line):
        """
        return a list of ip related geographical location data.
        """

        try:
            gi = pygeoip.GeoIP('GeoLiteCity.dat')
        except IOError:
            print 'Missing GeoLiteCity.dat file'
            exit(1)

        ip = line.split('-')[0].strip()
        geo_record = gi.record_by_addr(ip)

        return [ip, geo_record['country_name'], geo_record['country_code'],
            geo_record['city']]

    def get_time(self, line):
        """
        return the date and time as it appears in the log
        """

        return re.search(r'\[[a-zA-Z0-9/:]+', line).group()[1:-7]

    def get_request_type(self, line):
        """
        return the http verb associated with a request
        """

        request_type = re.search(r'"[GETPOSUDHAL]{3, 4}', line)
        if request_type:
            return [request_type.group()[1:]]
        else:
            return [re.search(r'".+?"', line).group()]

    def get_request_response(self, line):
        """
        return the http response code
        """

        request_response = re.search(r'\s{1}[2345][0-9]{2}\s{1}', line)
        if request_response:
            return request_response.group().strip()
        else:
            return null

    def get_reply_size(self, line):
        """
        return the reply size in bytes
        """


        return re.search(r'\d+', re.search(r'\d{1,5} "', bulk_rest).group()).group()

    def get_request_path(self, line):
        """
        return the queried path
        """

        request_path = re.search(r'\s(\/[a-zA-Z0-9-_\/\!\@\#\$\%\^\*\.]+|\/\s)', line)
        if request_path:
            return request_path.group().strip()
        else:
            return 'No request path?'

    def get_user_agent(self, line):
        """
        return the user agent
        """
        
        return line.split('"')[-2].replace(',', '.')






