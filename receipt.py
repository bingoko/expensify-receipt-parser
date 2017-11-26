import os
import csv
import urllib
import sys

# read the csv file
input_csv = sys.argv[1]
if not os.path.isfile(input_csv):
	print('Input CSV file \"' + input_csv + '\" does not exist')
	sys.exit()
	
f = open(input_csv, 'rb')
reader = csv.reader(f)

# skip the headers
next(reader, None) 

for row in reader:
	size = len(row)
	download_url = row[size-1]
	file_name = download_url.split('/')[-1]
	
	file_date = row[0].split('T')[0]
	file_year = row[0].split('-')[0]
	file_month = row[0].split('-')[1]
	file_path = file_year + '/' + file_year + '-' + file_month + '/' +file_name
	print file_date, file_path
	
	if not os.path.exists(file_year):
		os.makedirs(file_year)

	if not os.path.exists(file_year + '/' + file_year + '-' + file_month):
		os.makedirs(file_year + '/' + file_year + '-' + file_month)

	receipt_file = urllib.URLopener()
	receipt_file.retrieve(download_url, file_year + '/' + file_year + '-' + file_month + '/' +file_name)
f.close()