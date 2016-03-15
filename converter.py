with open('pw.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile)
	for row in spamreader:
		print (row['login'], row['Password'])
