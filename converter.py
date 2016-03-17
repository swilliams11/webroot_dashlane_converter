import csv

#with open('C:\Users\logikalone1\Documents\TEMP\pw.csv', 'rb') as csvfile:
csvfile = open('pw.csv', 'rb')
f = open('pwoutput.csv', 'wb')
writer = csv.writer(f)
	#writer.writerows(someiterable)

spamreader = csv.DictReader(csvfile)
writer.writerow(("Website", "Name", "Login", "Login2", "Password", "Category", "Note"))
for row in spamreader:
	#print (row['Username'], row['Password'], row['URL'], row['Name'], row['Notes '])
	writer.writerow((row['URL'],row['Name'], row['Username'], '',row['Password'],'',row['Notes '] ))

csvfile.close()
f.close()
