import csv
import numpy as np
import datetime


# importing csv module 
import csv 
  
# csv file name 
filename = "FAHTest.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
	csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
	fields = next(csvreader) 
  
    # extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 
  
    # get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 


PPD = []
projID = []
Assigned = []
Finished = []
Credit = []


for row in rows[1:200]:
		PPD.append(float(row[23]))

for row in rows[1:200]:
		projID.append(int(row[1]))
		
for row in rows[1:200]:
		Assigned.append(row[13])
		
for row in rows[1:200]:
		Finished.append(row[14])
		
for row in rows[1:200]:
		Credit.append(float(row[24]))
						
print(PPD[1])
print(projID[1])
print(Assigned[1])
print(Finished[1])
print(Credit[1])

date_time_obj_assigned = datetime.datetime.strptime(str(Assigned[1]), '%m/%d/%Y %H:%M')
date_time_obj_finished = datetime.datetime.strptime(str(Finished[1]), '%m/%d/%Y %H:%M')

#print('Date:', date_time_obj_assigned.date())
#print('Time:', date_time_obj_assigned.time())
#print('Date-time:', date_time_obj_assigned)

#print('Date:', date_time_obj_finished.date())
#print('Time:', date_time_obj_finished.time())
#print('Date-time:', date_time_obj_finished)

elapsedTime = date_time_obj_finished - date_time_obj_assigned

print(elapsedTime.total_seconds())

elapsedTimeSec = []

for i in range(1,199):
	date_time_obj_assigned = datetime.datetime.strptime(str(Assigned[i]), '%m/%d/%Y %H:%M')
	date_time_obj_finished = datetime.datetime.strptime(str(Finished[i]), '%m/%d/%Y %H:%M')
	elapsedTime = date_time_obj_finished - date_time_obj_assigned
	elapsedTimeSec.append(int(elapsedTime.total_seconds()))
	print(elapsedTimeSec[i-1])





























