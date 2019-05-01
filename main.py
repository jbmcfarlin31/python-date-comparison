from datetime import date,time,timedelta,datetime

def get_remaining_days(end_date, begin_date=date.today()):
	""" Computes the date differences and returns the output """
	mydate = end_date

	month = mydate.split("/")[0]
	day = mydate.split("/")[1]
	year = mydate.split("/")[2]

	end_date = date(day=int(day), month=int(month), year=int(year))

	date_diff = end_date - begin_date

	return date_diff

cruise = get_remaining_days(end_date="5/23/2019")
hawaii = get_remaining_days(end_date="6/25/2019")
utah = get_remaining_days(end_date="8/23/2019")

print("You have {} until your cruise!".format(cruise))
print("You have {} until you go to Hawaii!".format(hawaii))
print("You have {} until you go to Utah!".format(utah))
