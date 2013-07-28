      # Setup user input and output files
  # script, input, output = argv
  #so derty here

  f = open(input, 'rb')
  lines = f.readlines()
  f.close()

  out = open('%s.csv' % output, 'wb')
  # ip_out = open('%s_ip.csv' % output, 'wb')
  # path_out = open('%s_path.csv' % output, 'wb')

  writer = Csv(out)

  gi = pygeoip.GeoIP('GeoLiteCity.dat')

  # ips = PopularItem()
  # paths = PopularItem()

  # Main routine
  # try:
  for i in lines:
      chopped = i.split('-')
      split = i.split('"')
      ip = chopped[0].strip()
      geoip = gi.record_by_addr(ip)
      country = geoip['country_name']
      country_code = geoip['country_code']
      city = geoip['city']

      # ips.insert(ip)
        
      time = re.search(r'\[[a-zA-Z0-9/:]+', i).group()[1:-7]
      #arbitrary number to make parsing a wee bit easier
      bulk_rest = i[25:]
          try:
          request_type = re.search(r'"[GETPOSUDHAL]{3,4}', bulk_rest).group()[1:]
      except AttributeError, e:
          print "Request type error: ", e
          request_type = re.search(r'".+?"', bulk_rest).group()
          print request_type
      try:
          request_response = re.search(r'\s{1}[2345][0-9]{2}\s{1}', bulk_rest).group().strip()
      except:
          request_response = 'error'
      try:
          request_path = re.search(r'\s(\/[a-zA-Z0-9-_\/\!\@\#\$\%\^\*\.]+|\/\s)', bulk_rest).group().strip()
      except AttributeError, e:
          print 'Error: ', e
          print bulk_rest
          request_path = 'No request path?'

      # paths.insert(request_path)

      request_reply_size = re.search(r'\d+', re.search(r'\d{1,5} "', bulk_rest).group()).group()
      agent = split[-2].replace(',', '.')
      # write vs insert
      writer.insert([ip, country, country_code, city,
                  time, request_type, request_response, request_reply_size,
                  request_path, agent])

  writer.output_list()

  js = open('countries.js', 'wb')
  ToJson(js, writer.master_list, 1)
  js.close()


  writer.close()
  # writer = Csv(ip_out)
  # for ip, frequency in ips.master_list.iteritems():
  #   writer.write([ip, frequency])
  # writer.close()
  # writer = Csv(path_out)
  # for path, frequency in paths.master_list.iteritems():
  #   writer.write([path, frequency])
  # writer.close()
  print 'Created %s.csv' % output
  # except:
  #   print 'error'
  #   out.close()
  #   exit(1)
  # out.close()
