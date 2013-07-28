import re
import pygeoip
import json
from sys import argv

class Csv(object):
	def __init__(self, file):
		"""
		Accepts a file object for writing
		"""
		self.file = file
		self.master_list = []

	def write(self, row):
		"""
		Write a csv row of data to a file.
		"""
		row = [unicode(i) for i in row]
		s = ','.join(row) + '\n'
		self.file.write(s.encode('utf-8'))

	def insert(self, row):
		"""
		Insert a row into a list residing in memory.
		"""
		self.master_list.append(row)
		# self.master_list.append(','.join([unicode(i) for i in row]) + '\n')

	def output_list(self):
		"""
		Write in-memory list of values to file
		"""
		for i in self.master_list:
			self.file.write((','.join([unicode(j) for j in i]) + '\n').encode('utf-8'))
		# for i in self.master_list:
			# self.file.write(i.encode('utf-8'))

	def close(self):
		self.file.close()

class ToJson(object):
	def __init__(self, file, csv, column):
		"""
		Scan a Csv master_list, build a col:quantity list, 
		write it to JSON in [{item:quantity}] format.
		"""

		#this has to pair up the data in another fashion ie
		#[{country: item, hits: quantity}]. User dict(zip(row, key))
		self.file = file
		self.csv = csv
		self.col = column
		self.master_list = []

		popular_item = PopularItem()
		for i in self.csv:
			popular_item.insert(i[self.col])
		file.write(json.dumps([{col: quantity} for col, quantity in popular_item.master_list.iteritems()]))

	# def insert(self, row):
	# 	#user zip to combine key with row
	# 	#dict(zip(row, key))

class PopularItem(object):
	def __init__(self):
		self.master_list = {}

	def insert(self, item):
		if item in self.master_list:
			self.master_list[item] += 1
		else:
			self.master_list[item] = 1



# class nginx_log(object):

# 		# Setup user input and output files
# 	# script, input, output = argv

# 	f = open(input, 'rb')
# 	lines = f.readlines()
# 	f.close()

# 	out = open('%s.csv' % output, 'wb')
# 	# ip_out = open('%s_ip.csv' % output, 'wb')
# 	# path_out = open('%s_path.csv' % output, 'wb')

# 	writer = Csv(out)

# 	gi = pygeoip.GeoIP('GeoLiteCity.dat')

# 	# ips = PopularItem()
# 	# paths = PopularItem()

# 	# Main routine
# 	# try:
# 	for i in lines:
# 		chopped = i.split('-')
# 		split = i.split('"')
# 		ip = chopped[0].strip()
# 		geoip = gi.record_by_addr(ip)
# 		country = geoip['country_name']
# 		country_code = geoip['country_code']
# 		city = geoip['city']

# 		# ips.insert(ip)
		
# 		time = re.search(r'\[[a-zA-Z0-9/:]+', i).group()[1:-7]
# 		#arbitrary number to make parsing a wee bit easier
# 		bulk_rest = i[25:]
# 	        try:
# 			request_type = re.search(r'"[GETPOSUDHAL]{3,4}', bulk_rest).group()[1:]
# 		except AttributeError, e:
# 			print "Request type error: ", e
# 			request_type = re.search(r'".+?"', bulk_rest).group()
# 			print request_type
# 		try:
# 			request_response = re.search(r'\s{1}[2345][0-9]{2}\s{1}', bulk_rest).group().strip()
# 		except:
# 			request_response = 'error'
# 		try:
# 			request_path = re.search(r'\s(\/[a-zA-Z0-9-_\/\!\@\#\$\%\^\*\.]+|\/\s)', bulk_rest).group().strip()
# 		except AttributeError, e:
# 			print 'Error: ', e
# 			print bulk_rest
# 			request_path = 'No request path?'

# 		# paths.insert(request_path)

# 		request_reply_size = re.search(r'\d+', re.search(r'\d{1,5} "', bulk_rest).group()).group()
# 		agent = split[-2].replace(',', '.')
# 		# write vs insert
# 		writer.insert([ip, country, country_code, city,
# 					time, request_type, request_response, request_reply_size,
# 					request_path, agent])

# 	writer.output_list()

# 	js = open('countries.js', 'wb')
# 	ToJson(js, writer.master_list, 1)
# 	js.close()


# 	writer.close()
# 	# writer = Csv(ip_out)
# 	# for ip, frequency in ips.master_list.iteritems():
# 	# 	writer.write([ip, frequency])
# 	# writer.close()
# 	# writer = Csv(path_out)
# 	# for path, frequency in paths.master_list.iteritems():
# 	# 	writer.write([path, frequency])
# 	# writer.close()
# 	print 'Created %s.csv' % output
# 	# except:
# 	# 	print 'error'
# 	# 	out.close()
# 	# 	exit(1)
	# out.close()

