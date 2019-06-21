Readme
1. sp_evite
Executes two procedures
	-crevite - imports data from guestlist from Evite
		-fixbadchar - removes special characters from notes section
	-modifyguests - updates guests table with new values from RSVP and notes fields
2. evitecsvmod.py
Transfers contents of guestlist.csv to new file eviteguests.csv.  Removes files with filename of guestlist.csv and RSVPUpdates.csv
3. rsvpemail.py
Emails RSVPUpdates.csv which shows all updates that have been made.  This CSV is created by stored procedure - modifyguests.
4. sp_addressreport 
Create CSV of all residents with no address
5. Single guest address procedures
Inserts records in guestmailinginfo table for single guests.
-singleguestaddress2 - Stored procedure for single guests with an address
-singleguestaddress4 -Stored procedure for single guests with no address
6. Couples guest address procedures
Inserts records in guestmailinginfo table for couples.
-coupleguestaddress - Stored procedure for couples with an address
	-firstnamelist - Function that creates list of first names for guests with same last name and a particular address
	-partycount - Function that takes count of guests with same last name and address
-coupleguestaddressmod2 - Stored procedure for couples with no address
	-firstnamelist2 - Function that creates list of first names for guests with same last name
	-partycount2 - Function that takes count of guests with same last name 
7. sp_numberinparty 
Create guest count card with guest names and party count.
8. mailingaddress
This stored procedure executes all mailing address stored procedures
9. sp_mailinglabels  
This stored procedure creates the mailing labels from guestmailinginfo table.