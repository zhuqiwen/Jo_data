import csv
import pprint as pp
import plotly.graph_objs as g_o
import time
import sys

on_off_line = raw_input('Publish the chart onto plotly.com? (y/n)')
if on_off_line.lower() == 'y':
	from plotly.plotly import plot
elif on_off_line.lower() == 'n':
	from plotly.offline import plot
else:
	sys.exit("unrecognized answer!Re-run the script again!\n")

# from plotly.offline import plot   # use this import if offline/for offline test
# from plotly.plotly import plot    #use this to publish chart onto plotly.com




def get_sleeptime(sleepfile):
	with open(sleepfile) as f:
		content = csv.DictReader(f)
		sleep_dict = {}
		for row in content:
			date = (row['Time'].split(',')[0])
			date = time.strftime("%m/%d/%y",time.strptime(date, "%m/%d/%y")) # change date format from "2/23/16" to "02/23/16", convenient for sorting date
			durations = row['Duration(minutes)']
			sleep_dict.setdefault(date,[]).append(durations)
		for d in sleep_dict.keys():
			dura_total = sum(map(int, sleep_dict[d]))
			sleep_dict[d] = (dura_total, sleep_dict[d])


		return sleep_dict

sleep_dict = get_sleeptime('Jo_sleep.csv')

print sleep_dict

date =[]
for d in sleep_dict.keys():
	d = time.strftime("%m/%d/%y",time.strptime(d, "%m/%d/%y"))
	date.append(d)
date.sort()
print date

duration = []
for d in date:
	duration.append(sleep_dict[d][0]/60)
# print duration



data = [g_o.Bar(x = date, y=duration)]

plot(data) 