from optparse import OptionParser
from nginxgraph import Nginxgraph
from statfile import StatFile

def main():

    OPTION_INDICES = { 'ip': 0, 'nation': 1, 'method': 5, 'user_agent': 9 ,
                        'reply_status': 6, 'stadt': 3 }

    VERSION = '0.1'

    parser = OptionParser()
    parser.add_option('-c', '--csv',
                        help='Outputs data into a csv file',
                        action='store_true')
    parser.add_option('-j', '--json',
                        help='Outputs data into a json file',
                        action='store_true')

    parser.add_option('-a', '--all',
                        help='Outputs a file with all data',
                        action='store_true')
    parser.add_option('-i', '--ip',
                        help='Outputs file with IP count',
                        action='store_true')
    parser.add_option('-n', '--nation',
                        help='Outputs file with country count',
                        action='store_true')
    parser.add_option('-m', '--method',
                        help='Outputs file with http verb count',
                        action='store_true')
    parser.add_option('-u', '--user_agent',
                        help='Outputs file with user agent count',
                        action='store_true')
    parser.add_option('-r', '--reply_status',
                        help='Outputs file with reply status count',
                        action='store_true')
    parser.add_option('-s', '--stadt',
                        help='Outputs file with city count (might have blanks',
                        action='store_true')

    (options, args) = parser.parse_args()

    if len(args) == 0 or options.csv == None and options.json == None:
        print "Must input log file or choose csv/json"
        exit(1)
    print options

    try:
        f = open(args[0])
    except IOError, e:
        print e
        exit(1)
    lines = f.readlines()
    f.close()

    parser = Nginxgraph()
    data_list = parser.analyze_log(lines)

if __name__ == '__main__':
    main()