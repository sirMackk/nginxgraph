from optparse import OptionParser

def main():
    parser = OptionParser()

    parser.add_option('-c', '--csv', help='Outputs data into a csv file', action="store_true")
    parser.add_option('-j', '--json', help='Outputs data into a json file', action="store_true")

    parser.add_option('-a', '--all', help="Outputs a file with all data", action="store_true")
    parser.add_option('-i', '--ip', help='Outputs file with IP count', action="store_true")
    parser.add_option('-n', '--nation', help='Outputs file with country count', action="store_true")
    parser.add_option('-m', '--method', help='Outputs file with http verb count', action="store_true")
    parser.add_option('-u', '--user_agent', help='Outputs file with user agent count', action="store_true")

    (options, args) = parser.parse_args()

    if len(args) == 0 or options.csv == None and options.json == None:
        print "Must input log file or choose csv/json"
        exit(1)

if __name__ == '__main__':
    main()