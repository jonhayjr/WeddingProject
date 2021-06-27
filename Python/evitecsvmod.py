--Transfers contens of guestlist.csv to new file eviteguests.csv
--Removes files with filename of guestlist.csv and RSVPUpdates.csv
import os
import csv
oldcsv = open('C:\\Users\\Downloads\\guestlist.csv', 'r', encoding = 'utf-8')
oldreader = csv.reader(oldcsv, delimiter = ',')
newcsv = open('C:\\Import\\eviteguests.csv', 'w', encoding = 'utf-8', newline = '')
newwriter = csv.writer(newcsv)
for row in oldreader:

	newwriter.writerow ([row[0], row[1], row[2], row[3], row[4], row[5]])


oldcsv.close()
newcsv.close()

os.remove('C:\\Users\Downloads\\guestlist.csv')
os.remove('C:\\Exports\\RSVPUpdates.csv')
print("Files Removed!")


