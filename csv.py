import csv
import os


read_into_dict = False

file_name = 'test.csv'
file_path = os.path.join(os.getcwd(), file_name)


with open(file_path) as r:
	# Read (and skip) the first line if it is a non-CSV value.
	fist_line = r.readline()

	if read_into_dict:
		reader = csv.DictReader(r)

		# Each row is a dict of values.
		for row in reader:
			print(row)

	else:
		reader = csv.reader(r)

		# Skip first row if you want to ignore headings.
		next(reader)

		# Each row is a list of values.
		for row in reader:
			print(row)
