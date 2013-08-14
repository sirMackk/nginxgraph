import pygeoip
import json

class StatFile(object):
	def __init__(self, file_name):
		self.file_name = file_name
		self.master_list = []
		self.log_key = ['ip', 'country', 'city', 'datetime', 'method', 'http_status', 
						'reply_size', 'user_agent']

	def append_to_list(self, row):
		"""
		Insert a row into a list residing in memory.
		"""
		self.master_list.append(row)

	def make_csv(self, items):
		"""
		Write list to csv file
		"""
		f = open('%s.csv' % self.file_name, 'wb')
		for i in items:
			f.write((','.join([unicode(j) for j in i]) + '\n').encode('utf-8'))
		f.close()

	def make_json(self, items):
		"""
		Write list to json array file
		"""
		f = open('%s.js' % self.file_name, 'wb')
		f.write(json.dumps(items))
		f.close()

	def write_csv(self):
		"""
		Write in-memory list of values to csv file
		"""
		self.make_csv(self.master_list)

	def write_json(self):
		"""
		Write in-memory list of values to json array file
		"""
		self.make_json([dict(zip(self.log_key, i)) for i in self.master_list])


	def popular(self, column_number):
		"""
		Return a dictionary representing popular items
		ie. item:count
		"""
		popular = {}
		for i in self.master_list:
			if i[column_number] in popular:
				popular[i[column_number]] += 1
			else:
				popular[i[column_number]] = 1	
		
		return popular	

	def csv_popular_column(self, column_number):
		"""
		Count and write the most popular items from master_list
		into a csv file
		"""
		self.make_csv([i for i in self.popular(column_number).iteritems()])

	def json_popular_column(self, column_number):
		"""
		Count and write the most popular items from master_list
		into a json .js file
		"""
		self.make_json([{"key": key, "value": value} for key, value 
					in self.popular(column_number).iteritems()])
